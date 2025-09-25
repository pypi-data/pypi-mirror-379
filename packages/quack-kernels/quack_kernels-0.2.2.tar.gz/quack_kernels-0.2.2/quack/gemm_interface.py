# Copyright (c) 2025, Tri Dao
from typing import Optional, Tuple, Literal
from functools import partial

import torch
import torch.nn.functional as F
from torch import Tensor

from quack.gemm_config import GemmConfig, get_all_configs

from quack.autotuner import autotune, AutotuneConfig
from quack.dense_gemm_sm90 import gemm_sm90
from quack.gemm_act_sm90 import gemm_act_sm90
from quack.gemm_dact_sm90 import gemm_dact_sm90


# Dictionary mapping activation names to PyTorch functions
act_to_pytorch_fn_map = {
    None: lambda x: x,
    "relu": F.relu,
    "relu_sq": lambda x: F.relu(x).square(),
    "gelu_tanh_approx": partial(F.gelu, approximate="tanh"),
}


# Dictionary mapping gated activation names to their forward functions
# Each function takes (gate, up) and returns postact
gated_to_pytorch_fn_map = {
    "swiglu": lambda gate, up: F.silu(gate) * up,
    "swiglu_oai": lambda gate, up: gate * torch.sigmoid(1.702 * gate) * (up + 1),
    "reglu": lambda gate, up: F.relu(gate) * up,
    "geglu": lambda gate, up: F.gelu(gate, approximate="tanh") * up,
    "glu": lambda gate, up: torch.sigmoid(gate) * up,
}


def prune_invalid_gemm_configs(configs, named_args: dict, **kwargs):
    kwargs = named_args | kwargs
    gather_A = kwargs.get("A_idx", None) is not None
    varlen_m = kwargs.get("cu_seqlens_m", None) is not None
    if varlen_m or gather_A:  # Doesn't support swap_ab
        configs = [conf for conf in configs if not conf.kwargs["config"].swap_ab]
    if gather_A:
        # tile_n == 208 causes register spills, as gather_A requires more registers for the producer
        configs = [
            conf
            for conf in configs
            if conf.kwargs["config"].cluster_n == 1 and conf.kwargs["config"].tile_n != 208
        ]
    return configs


@autotune(
    configs=[AutotuneConfig(config=c) for c in get_all_configs()],
    key=["dynamic_scheduler"],
    prune_configs_by={"early_config_prune": prune_invalid_gemm_configs},
)
def gemm_tuned(
    # (M, K) or (L, M, K) or (total_M, K) if varlen_m or (M, total_K) if varlen_k or (whatever, K) if gather_A with varlen_m or (M, whatever) if gather_A with varlen_k
    A: Tensor,
    B: Tensor,  # (K, N) or (L, K, N) or (total_K, N) if varlen_k
    out: Tensor,  # (M, N) or (L, M, N) or (total_M, N) if varlen_m
    C: Optional[Tensor] = None,  # (M, N) or (L, M, N) or (total_M, N) if varlen_m
    alpha: float | Tensor = 1.0,  # (1,)
    beta: float | Tensor = 1.0,  # (1,)
    cu_seqlens_m: Optional[Tensor] = None,  # (L+1), int32
    cu_seqlens_k: Optional[Tensor] = None,  # (L+1), int32
    A_idx: Optional[Tensor] = None,  # (total_M,) or (total_K,) indices for gather_A when varlen
    batch_idx_permute: Optional[Tensor] = None,  # (L,) permutation of batch indices for scheduler
    add_to_output: bool = False,
    dynamic_scheduler: bool = False,
    config: Optional[GemmConfig] = None,
) -> None:
    if config is None:
        config = GemmConfig(tile_m=128, tile_n=192, cluster_m=2, cluster_n=1, pingpong=True)
    varlen_m = cu_seqlens_m is not None
    varlen_k = cu_seqlens_k is not None
    varlen = varlen_m or varlen_k
    gather_A = A_idx is not None
    if gather_A:
        assert varlen, "gather_A requires either varlen_m or varlen_k"
        assert config.cluster_n == 1, "gather_A requires cluster_n=1"
    if varlen_m:
        assert not config.swap_ab, "Variable-length sequences not supported with swap_ab"
    if A.ndim == 2 and not varlen:
        A = A.unsqueeze(0)  # (1, M, K)
    B = B.mT  # (N, K) or (L, N, K) or (N, total_K)
    if B.ndim == 2 and not varlen_k:
        B = B.unsqueeze(0)  # (1, N, K)
    if C is not None and C.ndim == 2 and not varlen_m:
        C = C.unsqueeze(0)  # (1, M, N)
    if out.ndim == 2 and not varlen_m:
        out = out.unsqueeze(0)
    batch_size = B.shape[0] if not varlen_k else cu_seqlens_k.shape[0] - 1
    if varlen_m:
        # If gather_A (A_idx provided), use its length; otherwise use A.shape[0]
        total_m = A_idx.shape[0] if A_idx is not None else A.shape[0]
        out_shape = (total_m, B.shape[-2])
    else:
        out_shape = (batch_size, A.shape[-2], B.shape[-2])
    assert out.shape == out_shape, f"out shape mismatch: {out.shape} vs {out_shape}"
    tile_count_semaphore = (
        torch.zeros(1, dtype=torch.int32, device=A.device) if dynamic_scheduler else None
    )
    gemm_sm90(
        A if not config.swap_ab else B,
        B if not config.swap_ab else A,
        out if not config.swap_ab else out.mT,
        (C if not config.swap_ab else C.mT) if C is not None else None,
        tile_count_semaphore,
        config.tile_m,
        config.tile_n,
        config.cluster_m,
        config.cluster_n,
        config.pingpong,
        alpha=alpha,
        beta=beta,
        cu_seqlens_m=cu_seqlens_m,
        cu_seqlens_k=cu_seqlens_k,
        A_idx=A_idx,
        batch_idx_permute=batch_idx_permute,
        add_to_output=add_to_output,
    )


@autotune(
    configs=[AutotuneConfig(config=c) for c in get_all_configs()],
    key=["activation", "dynamic_scheduler"],
    prune_configs_by={"early_config_prune": prune_invalid_gemm_configs},
)
def gemm_act_tuned(
    # (M, K) or or (L, M, K) or (total_M, K) if varlen_m or (whatever, K) if gather_A with varlen_m
    A: Tensor,
    B: Tensor,  # (K, N) or (L, K, N)
    # (M, N) or (L, M, N) or (total_M, N) if varlen_m - None if not storing preact
    preact_out: Optional[Tensor],
    postact_out: Tensor,  # (M, N) or (L, M, N) or (total_M, N) if varlen_m
    C: Optional[Tensor] = None,  # (M, N) or (L, M, N) or (total_M, N) if varlen_m
    activation: Literal[None, "relu", "relu_sq", "gelu_tanh_approx"] = None,
    cu_seqlens_m: Optional[Tensor] = None,  # (L+1), int32
    A_idx: Optional[Tensor] = None,  # (total_M,) if gather_A with varlen_m
    dynamic_scheduler: bool = False,
    config: Optional[GemmConfig] = None,
) -> None:
    if config is None:
        config = GemmConfig(tile_m=128, tile_n=192, cluster_m=2, cluster_n=1, pingpong=True)
    varlen_m = cu_seqlens_m is not None
    if varlen_m:
        assert not config.swap_ab, "Variable-length sequences not supported with swap_ab"
    if A.ndim == 2 and not varlen_m:
        A = A.unsqueeze(0)  # (1, M, K)
    B = B.mT  # (N, K) or (L, N, K)
    if B.ndim == 2:
        B = B.unsqueeze(0)  # (1, N, K)
    if C is not None and C.ndim == 2 and not varlen_m:
        C = C.unsqueeze(0)  # (1, M, N)
    if preact_out is not None and preact_out.ndim == 2 and not varlen_m:
        D = preact_out.unsqueeze(0)
    else:
        D = preact_out
    if postact_out.ndim == 2 and not varlen_m:
        PostAct = postact_out.unsqueeze(0)
    else:
        PostAct = postact_out
    tile_count_semaphore = (
        torch.zeros(1, dtype=torch.int32, device=A.device) if dynamic_scheduler else None
    )
    gemm_act_sm90(
        A if not config.swap_ab else B,
        B if not config.swap_ab else A,
        (D if not config.swap_ab else D.mT) if D is not None else None,
        (C if not config.swap_ab else C.mT) if C is not None else None,
        PostAct if not config.swap_ab else PostAct.mT,
        tile_count_semaphore,
        activation,
        config.tile_m,
        config.tile_n,
        config.cluster_m,
        config.cluster_n,
        config.pingpong,
        persistent=True,
        cu_seqlens_m=cu_seqlens_m,
        A_idx=A_idx,
    )


@autotune(
    configs=[AutotuneConfig(config=c) for c in get_all_configs()],
    key=["activation", "dynamic_scheduler"],
    prune_configs_by={"early_config_prune": prune_invalid_gemm_configs},
)
def gemm_dact_tuned(
    # (M, K) or or (L, M, K) or (total_M, K) if varlen_m or (whatever, K) if gather_A with varlen_m
    A: Tensor,
    B: Tensor,  # (K, N) or (L, K, N)
    PreAct: Tensor,  # (M, N) or (L, M, N) or (total_M, N) if varlen_m
    dx_out: Tensor,  # (M, N) or (L, M, N) or (total_M, N) if varlen_m
    postact_out: Tensor,  # (M, N) or (L, N, N) or (total_M, N) if varlen_m
    activation: Literal[None, "relu", "relu_sq", "gelu_tanh_approx"] = None,
    cu_seqlens_m: Optional[Tensor] = None,  # (L+1), int32
    A_idx: Optional[Tensor] = None,  # (total_M,) if gather_A with varlen_m
    dynamic_scheduler: bool = True,
    config: Optional[GemmConfig] = None,
) -> None:
    if config is None:
        config = GemmConfig(tile_m=128, tile_n=192, cluster_m=2, cluster_n=1, pingpong=True)
    varlen_m = cu_seqlens_m is not None
    if varlen_m:
        assert not config.swap_ab, "Variable-length sequences not supported with swap_ab"
    if A.ndim == 2 and not varlen_m:
        A = A.unsqueeze(0)  # (1, M, K)
    B = B.mT  # (N, K) or (L, N, K)
    if B.ndim == 2:
        B = B.unsqueeze(0)  # (1, N, K)
    if PreAct.ndim == 2 and not varlen_m:
        PreAct = PreAct.unsqueeze(0)  # (1, M, N)
    if dx_out.ndim == 2 and not varlen_m:
        D = dx_out.unsqueeze(0)
    else:
        D = dx_out
    if postact_out.ndim == 2 and not varlen_m:
        PostAct = postact_out.unsqueeze(0)
    else:
        PostAct = postact_out
    tile_count_semaphore = (
        torch.zeros(1, dtype=torch.int32, device=A.device) if dynamic_scheduler else None
    )
    gemm_dact_sm90(
        A if not config.swap_ab else B,
        B if not config.swap_ab else A,
        D if not config.swap_ab else D.mT,
        PreAct if not config.swap_ab else PreAct.mT,
        PostAct if not config.swap_ab else PostAct.mT,
        tile_count_semaphore,
        activation,
        config.tile_m,
        config.tile_n,
        config.cluster_m,
        config.cluster_n,
        config.pingpong,
        persistent=True,
        cu_seqlens_m=cu_seqlens_m,
        A_idx=A_idx,
    )


def gemm(
    # (M, K) or (L, M, K) or (total_M, K) if varlen_m or (M, total_K) if varlen_k or (whatever, K) if gather_A with varlen_m or (M, whatever) if gather_A with varlen_k
    A: Tensor,
    B: Tensor,  # (K, N) or (L, K, N) or (total_K, N) if varlen_k
    out: Optional[Tensor] = None,  # (M, N) or (L, M, N) or (total_M, N) if varlen_m
    alpha: float | Tensor = 1.0,
    out_dtype: Optional[torch.dtype] = None,
    cu_seqlens_m: Optional[Tensor] = None,
    cu_seqlens_k: Optional[Tensor] = None,
    A_idx: Optional[Tensor] = None,  # (total_M,) or (total_K,) indices for gather_A when varlen
    batch_idx_permute: Optional[Tensor] = None,  # (L,) permutation of batch indices for scheduler
    dynamic_scheduler: bool = False,
    tuned: bool = True,
) -> Tensor:
    """GEMM with optional output tensor and tuning control."""
    if out is None:
        out_dtype = A.dtype if out_dtype is None else out_dtype
        varlen_m = cu_seqlens_m is not None
        varlen_k = cu_seqlens_k is not None
        if varlen_m:
            total_m = A_idx.shape[0] if A_idx is not None else A.shape[0]
            out_shape = (total_m, B.shape[-1])
        elif varlen_k:
            L = cu_seqlens_k.shape[0] - 1
            # For varlen_k, the first dimension is always A.shape[0] (M dimension)
            out_shape = (L, A.shape[0], B.shape[-1])
        else:
            out_shape = (
                (A.shape[0], B.shape[-1]) if A.ndim == 2 else (A.shape[0], A.shape[-2], B.shape[-1])
            )
        out = torch.empty(out_shape, dtype=out_dtype, device=A.device)
    alpha_tensor = alpha if not isinstance(alpha, float) else None
    alpha = alpha if isinstance(alpha, float) else 1.0
    gemm_out(
        A,
        B,
        out,
        alpha=alpha,
        alpha_tensor=alpha_tensor,
        cu_seqlens_m=cu_seqlens_m,
        cu_seqlens_k=cu_seqlens_k,
        A_idx=A_idx,
        batch_idx_permute=batch_idx_permute,
        dynamic_scheduler=dynamic_scheduler,
        tuned=tuned,
    )
    return out


@torch.library.custom_op(
    "quack::gemm_out",
    mutates_args=("out",),
    device_types="cuda",
    # We have to split out alpha and alpha_tensor since torch.library requires
    # each argument to have a fixed type
    # schema="(Tensor A, Tensor B, Tensor(a2!) out, float alpha=1.0, Tensor? alpha_tensor=None, bool dynamic_scheduler=False, bool tuned=True) -> ()",
)
def gemm_out(
    # (M, K) or (L, M, K) or (total_M, K) if varlen_m or (M, total_K) if varlen_k or (whatever, K) if gather_A with varlen_m or (M, whatever) if gather_A with varlen_k
    A: Tensor,
    B: Tensor,  # (K, N) or (L, K, N) or (total_K, N) if varlen_k
    out: Tensor,  # (M, N) or (L, M, N) or (total_M, N) if varlen_m
    alpha: float = 1.0,
    alpha_tensor: Optional[Tensor] = None,
    cu_seqlens_m: Optional[Tensor] = None,
    cu_seqlens_k: Optional[Tensor] = None,
    A_idx: Optional[Tensor] = None,  # (total_M,) or (total_K,) indices for gather_A when varlen
    batch_idx_permute: Optional[Tensor] = None,  # (L,) permutation of batch indices for scheduler
    dynamic_scheduler: bool = False,
    tuned: bool = True,
) -> None:
    """GEMM with pre-allocated output tensor."""
    fn = gemm_tuned if tuned else partial(gemm_tuned.fn, config=None)
    alpha = alpha_tensor if alpha_tensor is not None else alpha
    fn(
        A,
        B,
        out,
        C=None,
        alpha=alpha,
        cu_seqlens_m=cu_seqlens_m,
        cu_seqlens_k=cu_seqlens_k,
        A_idx=A_idx,
        batch_idx_permute=batch_idx_permute,
        dynamic_scheduler=dynamic_scheduler,
    )


def gemm_ref(
    # (M, K) or (L, M, K) or (total_M, K) if varlen_m or (M, total_K) if varlen_k or (whatever, K) if gather_A with varlen_m or (M, whatever) if gather_A with varlen_k
    A: Tensor,
    B: Tensor,  # (K, N) or (L, K, N) or (total_K, N) if varlen_k
    out: Optional[Tensor] = None,  # (M, N) or (L, M, N) or (total_M, N) if varlen_m
    alpha: float | Tensor = 1.0,
    cu_seqlens_m: Optional[Tensor] = None,
    cu_seqlens_k: Optional[Tensor] = None,
    A_idx: Optional[Tensor] = None,  # (total_M,) or (total_K,) indices for gather_A when varlen
    out_dtype: Optional[torch.dtype] = None,
) -> Tensor:
    """Reference implementation for GEMM with pre-allocated output."""
    # The out_dtype argument requires torch >= 2.8
    out_dtype = A.dtype if out_dtype is None else out_dtype
    if cu_seqlens_m is None and cu_seqlens_k is None:
        fn = torch.bmm if A.ndim == 3 else torch.mm
        out = fn(A, B, out_dtype=out_dtype, out=out)
    elif cu_seqlens_m is not None:
        # Handle varlen_m case
        if out is None:
            # When gather_A (A_idx provided), output size is determined by A_idx length
            total_m = A_idx.shape[0] if A_idx is not None else A.shape[0]
            out = torch.empty((total_m, B.shape[-1]), dtype=out_dtype, device=A.device)
        for i in range(cu_seqlens_m.shape[0] - 1):
            A_slice = (
                A[A_idx[cu_seqlens_m[i] : cu_seqlens_m[i + 1]]]
                if A_idx is not None
                else A[cu_seqlens_m[i] : cu_seqlens_m[i + 1]]
            )
            torch.mm(A_slice, B[i], out=out[cu_seqlens_m[i] : cu_seqlens_m[i + 1]])
    else:  # cu_seqlens_k is not None
        L = cu_seqlens_k.shape[0] - 1
        if out is None:
            out = torch.empty((L, A.shape[0], B.shape[1]), dtype=out_dtype, device=A.device)
        for i in range(L):
            A_slice = (
                A[:, A_idx[cu_seqlens_k[i] : cu_seqlens_k[i + 1]]]
                if A_idx is not None
                else A[:, cu_seqlens_k[i] : cu_seqlens_k[i + 1]]
            )
            torch.mm(A_slice, B[cu_seqlens_k[i] : cu_seqlens_k[i + 1], :], out=out[i])
    if not isinstance(alpha, float) or alpha != 1.0:
        out = out * alpha
    return out


def gemm_add(
    # (M, K) or (L, M, K) or (total_M, K) if varlen_m or (M, total_K) if varlen_k or (whatever, K) if gather_A with varlen_m or (M, whatever) if gather_A with varlen_k
    A: Tensor,
    B: Tensor,  # (K, N) or (L, K, N) or (total_K, N) if varlen_k
    C: Tensor,  # (M, N) or (L, M, N) or (total_M, N) if varlen_m or (L, M, N) if varlen_k
    out: Optional[Tensor] = None,  # (M, N) or (L, M, N) or (total_M, N) if varlen_m
    alpha: float | Tensor = 1.0,
    beta: float | Tensor = 1.0,
    out_dtype: Optional[torch.dtype] = None,
    cu_seqlens_m: Optional[Tensor] = None,
    cu_seqlens_k: Optional[Tensor] = None,
    A_idx: Optional[Tensor] = None,  # (total_M,) or (total_K,) indices for gather_A when varlen
    batch_idx_permute: Optional[Tensor] = None,  # (L,) permutation of batch indices for scheduler
    dynamic_scheduler: bool = False,
    tuned: bool = True,
) -> Tensor:
    """GEMM with addition and optional output tensor."""
    if out is None:
        out_dtype = A.dtype if out_dtype is None else out_dtype
        varlen_m = cu_seqlens_m is not None
        varlen_k = cu_seqlens_k is not None
        if varlen_m:
            # If A_idx is provided (gather_A), use its length; otherwise use A.shape[0]
            total_m = A_idx.shape[0] if A_idx is not None else A.shape[0]
            out_shape = (total_m, B.shape[-1])
        elif varlen_k:
            L = cu_seqlens_k.shape[0] - 1
            # For varlen_k, the first dimension is always A.shape[0] (M dimension)
            out_shape = (L, A.shape[0], B.shape[-1])
        else:
            out_shape = (
                (A.shape[0], B.shape[-1]) if A.ndim == 2 else (A.shape[0], A.shape[-2], B.shape[-1])
            )
        out = torch.empty(out_shape, dtype=out_dtype, device=A.device)
    add_to_output = C is out and isinstance(beta, float) and beta == 1.0 and cu_seqlens_m is None
    alpha_tensor = alpha if not isinstance(alpha, float) else None
    alpha = alpha if isinstance(alpha, float) else 1.0
    beta_tensor = beta if not isinstance(beta, float) else None
    beta = beta if isinstance(beta, float) else 1.0
    gemm_add_out(
        A,
        B,
        C if not add_to_output else None,
        out,
        alpha,
        beta,
        alpha_tensor,
        beta_tensor,
        cu_seqlens_m=cu_seqlens_m,
        cu_seqlens_k=cu_seqlens_k,
        A_idx=A_idx,
        batch_idx_permute=batch_idx_permute,
        add_to_output=add_to_output,
        dynamic_scheduler=dynamic_scheduler,
        tuned=tuned,
    )
    return out


@torch.library.custom_op(
    "quack::gemm_add_out",
    mutates_args=("out",),
    device_types="cuda",
    # We have to split out alpha and alpha_tensor since torch.library requires
    # each argument to have a fixed type
    # schema="(Tensor A, Tensor B, Tensor C, Tensor(a3!) out, float alpha=1.0, float beta=1.0, Tensor? alpha_tensor=None, Tensor? beta_tensor=None, Tensor? cu_seqlens_m=None, bool dynamic_scheduler=False, bool tuned=True) -> ()",
)
def gemm_add_out(
    # (M, K) or (L, M, K) or (total_M, K) if varlen_m or (M, total_K) if varlen_k or (whatever, K) if gather_A with varlen_m or (M, whatever) if gather_A with varlen_k
    A: Tensor,
    B: Tensor,  # (K, N) or (L, K, N) or (total_K, N) if varlen_k
    C: Tensor,  # (M, N) or (L, M, N) or (total_M, N) if varlen_m or (L, M, N) if varlen_k
    out: Tensor,  # (M, N) or (L, M, N) or (total_M, N) if varlen_m
    alpha: float = 1.0,
    beta: float = 1.0,
    alpha_tensor: Optional[Tensor] = None,
    beta_tensor: Optional[Tensor] = None,
    cu_seqlens_m: Optional[Tensor] = None,
    cu_seqlens_k: Optional[Tensor] = None,
    A_idx: Optional[Tensor] = None,  # (total_M,) or (total_K,) indices for gather_A when varlen
    batch_idx_permute: Optional[Tensor] = None,  # (L,) permutation of batch indices for scheduler
    add_to_output: bool = False,
    dynamic_scheduler: bool = False,
    tuned: bool = True,
) -> None:
    """GEMM with addition and pre-allocated output tensor."""
    fn = gemm_tuned if tuned else partial(gemm_tuned.fn, config=None)
    alpha = alpha_tensor if alpha_tensor is not None else alpha
    beta = beta_tensor if beta_tensor is not None else beta
    fn(
        A,
        B,
        out,
        C,
        alpha=alpha,
        beta=beta,
        cu_seqlens_m=cu_seqlens_m,
        cu_seqlens_k=cu_seqlens_k,
        A_idx=A_idx,
        batch_idx_permute=batch_idx_permute,
        add_to_output=add_to_output,
        dynamic_scheduler=dynamic_scheduler,
    )


def gemm_add_ref(
    # (M, K) or (L, M, K) or (total_M, K) if varlen_m or (M, total_K) if varlen_k or (whatever, K) if gather_A with varlen_m or (M, whatever) if gather_A with varlen_k
    A: Tensor,
    B: Tensor,  # (K, N) or (L, K, N) or (total_K, N) if varlen_k
    C: Tensor,  # (M, N) or (L, M, N) or (total_M, N) if varlen_m
    out: Optional[Tensor] = None,  # (M, N) or (L, M, N) or (total_M, N) if varlen_m
    alpha: float | Tensor = 1.0,
    beta: float | Tensor = 1.0,
    cu_seqlens_m: Optional[Tensor] = None,
    cu_seqlens_k: Optional[Tensor] = None,
    A_idx: Optional[Tensor] = None,  # (total_M,) or (total_K,) indices for gather_A when varlen
    out_dtype: Optional[torch.dtype] = None,
) -> Tensor:
    """Reference implementation for GEMM with addition and pre-allocated output."""
    if cu_seqlens_m is None and cu_seqlens_k is None:
        if isinstance(alpha, float) and isinstance(beta, float):
            return torch.addmm(C, A, B, out_dtype=out_dtype, alpha=alpha, beta=beta, out=out)
        else:
            out_dtype = (
                out.dtype if out is not None else (out_dtype if out_dtype is not None else A.dtype)
            )
            result = (alpha * (A @ B) + beta * C).to(out_dtype)
            if out is not None:
                out.copy_(result)
            return result
    elif cu_seqlens_m is not None:
        # Handle varlen_m case
        if out is None:
            # When gather_A (A_idx provided), output size is determined by A_idx length
            total_m = A_idx.shape[0] if A_idx is not None else A.shape[0]
            out_dtype = out_dtype if out_dtype is not None else A.dtype
            out = torch.empty((total_m, B.shape[-1]), dtype=out_dtype, device=A.device)
        for i in range(cu_seqlens_m.shape[0] - 1):
            A_slice = (
                A[A_idx[cu_seqlens_m[i] : cu_seqlens_m[i + 1]]]
                if A_idx is not None
                else A[cu_seqlens_m[i] : cu_seqlens_m[i + 1]]
            )
            C_slice = C[cu_seqlens_m[i] : cu_seqlens_m[i + 1]]
            out_slice = out[cu_seqlens_m[i] : cu_seqlens_m[i + 1]]
            result = alpha * torch.mm(A_slice, B[i]) + beta * C_slice
            out_slice.copy_(result)
    else:  # cu_seqlens_k is not None
        # Handle varlen_k case
        L = cu_seqlens_k.shape[0] - 1
        out_dtype = out_dtype if out_dtype is not None else A.dtype
        if out is None:
            out = torch.empty((L, A.shape[0], B.shape[1]), dtype=out_dtype, device=A.device)
        for i in range(L):
            A_slice = (
                A[:, A_idx[cu_seqlens_k[i] : cu_seqlens_k[i + 1]]]
                if A_idx is not None
                else A[:, cu_seqlens_k[i] : cu_seqlens_k[i + 1]]
            )
            B_slice = B[cu_seqlens_k[i] : cu_seqlens_k[i + 1], :]
            result = alpha * torch.mm(A_slice, B_slice) + beta * C[i]
            out[i].copy_(result)
    return out


def gemm_add_inplace(
    # (M, K) or (L, M, K) or (total_M, K) if varlen_m or (M, total_K) if varlen_k or (whatever, K) if gather_A with varlen_m or (M, whatever) if gather_A with varlen_k
    A: Tensor,
    B: Tensor,  # (K, N) or (L, K, N) or (total_K, N) if varlen_k
    out: Tensor,  # (M, N) or (L, M, N) or (total_M, N) if varlen_m or (L, M, N) if varlen_k
    alpha: float | Tensor = 1.0,
    beta: float | Tensor = 1.0,
    cu_seqlens_m: Optional[Tensor] = None,
    cu_seqlens_k: Optional[Tensor] = None,
    A_idx: Optional[Tensor] = None,  # (total_M,) or (total_K,) indices for gather_A when varlen
    batch_idx_permute: Optional[Tensor] = None,  # (L,) permutation of batch indices for scheduler
    dynamic_scheduler: bool = False,
    tuned: bool = True,
) -> None:
    """In-place GEMM with addition: out = alpha * A @ B + beta * out.
    Args:
        A: (M, K) or (L, M, K) or (total_M, K) if varlen_m or (M, total_K) if varlen_k - input tensor
        B: (K, N) or (L, K, N) or (total_K, N) if varlen_k - input tensor
        out: (M, N) or (L, M, N) or (total_M, N) if varlen_m or (L, M, N) if varlen_k - tensor to accumulate into (modified in-place)
        alpha: Scalar multiplier for A @ B
        beta: Scalar multiplier for out
        cu_seqlens_m: Optional cumulative sequence lengths for variable M
        cu_seqlens_k: Optional cumulative sequence lengths for variable K
        dynamic_scheduler: Whether to use dynamic scheduler
        tuned: Whether to use autotuned configuration
    """
    alpha_tensor = alpha if not isinstance(alpha, float) else None
    alpha = alpha if isinstance(alpha, float) else 1.0
    beta_tensor = beta if not isinstance(beta, float) else None
    beta = beta if isinstance(beta, float) else 1.0
    gemm_add_inplace_op(
        A,
        B,
        out,
        alpha,
        beta,
        alpha_tensor,
        beta_tensor,
        cu_seqlens_m,
        cu_seqlens_k,
        A_idx=A_idx,
        batch_idx_permute=batch_idx_permute,
        dynamic_scheduler=dynamic_scheduler,
        tuned=tuned,
    )


@torch.library.custom_op(
    "quack::gemm_add_inplace",
    mutates_args=("out",),
    device_types="cuda",
    # We have to split out alpha and alpha_tensor since torch.library requires
    # each argument to have a fixed type
    # schema="(Tensor A, Tensor B, Tensor(a2!) out, float alpha=1.0, float beta=1.0, Tensor? alpha_tensor=None, Tensor? beta_tensor=None, Tensor? cu_seqlens_m=None, bool dynamic_scheduler=False, bool tuned=True) -> ()",
)
def gemm_add_inplace_op(
    # (M, K) or (L, M, K) or (total_M, K) if varlen_m or (M, total_K) if varlen_k or (whatever, K) if gather_A with varlen_m or (M, whatever) if gather_A with varlen_k
    A: Tensor,
    B: Tensor,  # (K, N) or (L, K, N) or (total_K, N) if varlen_k
    out: Tensor,  # (M, N) or (L, M, N) or (total_M, N) if varlen_m or (L, M, N) if varlen_k
    alpha: float = 1.0,
    beta: float = 1.0,
    alpha_tensor: Optional[Tensor] = None,
    beta_tensor: Optional[Tensor] = None,
    cu_seqlens_m: Optional[Tensor] = None,
    cu_seqlens_k: Optional[Tensor] = None,
    A_idx: Optional[Tensor] = None,  # (total_M,) or (total_K,) indices for gather_A when varlen
    batch_idx_permute: Optional[Tensor] = None,  # (L,) permutation of batch indices for scheduler
    dynamic_scheduler: bool = False,
    tuned: bool = True,
) -> None:
    fn = gemm_tuned if tuned else partial(gemm_tuned.fn, config=None)
    alpha = alpha_tensor if alpha_tensor is not None else alpha
    beta = beta_tensor if beta_tensor is not None else beta
    add_to_output = isinstance(beta, float) and beta == 1.0 and cu_seqlens_m is None
    # Use out as both input bias and output
    fn(
        A,
        B,
        out,
        out if not add_to_output else None,
        alpha=alpha,
        beta=beta,
        cu_seqlens_m=cu_seqlens_m,
        cu_seqlens_k=cu_seqlens_k,
        A_idx=A_idx,
        batch_idx_permute=batch_idx_permute,
        add_to_output=add_to_output,
        dynamic_scheduler=dynamic_scheduler,
    )


def gemm_act(
    A: Tensor,  # (M, K) or (L, M, K) or (total_M, K) if varlen_m or (whatever, K) if gather_A with varlen_m
    B: Tensor,  # (K, N) or (L, K, N)
    C: Optional[Tensor] = None,  # (M, N) or (L, M, N) or (total_M, N) if varlen_m
    activation: Literal[None, "relu", "relu_sq", "gelu_tanh_approx"] = None,
    preact_out: Optional[Tensor] = None,  # (M, N) or (L, M, N) or (total_M, N) if varlen_m
    postact_out: Optional[Tensor] = None,  # (M, N) or (L, M, N) or (total_M, N) if varlen_m
    out_dtype: Optional[torch.dtype] = None,
    postact_dtype: Optional[torch.dtype] = None,
    cu_seqlens_m: Optional[Tensor] = None,
    A_idx: Optional[Tensor] = None,  # (total_M,) if gather_A with varlen_m
    store_preact: bool = True,
    dynamic_scheduler: bool = False,
    tuned: bool = True,
) -> Tuple[Optional[Tensor], Tensor]:
    """GEMM with activation and optional output tensors."""
    out_dtype = A.dtype if out_dtype is None else out_dtype
    postact_dtype = A.dtype if postact_dtype is None else postact_dtype
    varlen_m = cu_seqlens_m is not None
    # Determine output shape based on gather_A
    if varlen_m:
        total_m = A_idx.shape[0] if A_idx is not None else A.shape[0]
        out_shape = (total_m, B.shape[-1])
    elif A.ndim == 2:
        out_shape = (A.shape[0], B.shape[-1])
    else:
        out_shape = (A.shape[0], A.shape[-2], B.shape[-1])
    if preact_out is None and store_preact:
        preact_out = torch.empty(out_shape, dtype=out_dtype, device=A.device)
    if postact_out is None:
        postact_out = torch.empty(out_shape, dtype=postact_dtype, device=A.device)
    gemm_act_out(
        A, B, preact_out, postact_out, C, activation, cu_seqlens_m, A_idx, dynamic_scheduler, tuned
    )
    return preact_out, postact_out


@torch.library.custom_op(
    "quack::gemm_act_out",
    mutates_args=("preact_out", "postact_out"),
    device_types="cuda",
    schema="(Tensor A, Tensor B, Tensor(a2!)? preact_out, Tensor(a3!) postact_out, Tensor? C=None, str? activation=None, Tensor? cu_seqlens_m=None, Tensor? A_idx=None, bool dynamic_scheduler=False, bool tuned=True) -> ()",
)
def gemm_act_out(
    A: Tensor,  # (M, K) or (L, M, K) or (total_M, K) if varlen_m or (whatever, K) if gather_A with varlen_m
    B: Tensor,  # (K, N) or (L, K, N)
    preact_out: Optional[Tensor],  # (M, N) or (L, M, N) or (total_M, N) if varlen_m
    postact_out: Tensor,  # (M, N) or (L, M, N) or (total_M, N) if varlen_m
    C: Optional[Tensor] = None,  # (M, N) or (L, M, N) or (total_M, N) if varlen_m
    activation: Literal[None, "relu", "relu_sq", "gelu_tanh_approx"] = None,
    cu_seqlens_m: Optional[Tensor] = None,
    A_idx: Optional[Tensor] = None,  # (total_M,) if gather_A with varlen_m
    dynamic_scheduler: bool = False,
    tuned: bool = True,
) -> None:
    """GEMM with activation and pre-allocated output tensors."""
    fn = gemm_act_tuned if tuned else partial(gemm_act_tuned.fn, config=None)
    fn(A, B, preact_out, postact_out, C, activation, cu_seqlens_m, A_idx, dynamic_scheduler)


def gemm_act_ref(
    A: Tensor,  # (M, K) or (L, M, K) or (total_M, K) if varlen_m or (M, total_K) if varlen_k or (whatever, K) if gather_A
    B: Tensor,  # (K, N) or (L, K, N) or (total_K, N) if varlen_k
    C: Optional[Tensor] = None,  # (M, N) or (L, M, N) or (total_M, N) if varlen_m
    activation: Literal[None, "relu", "relu_sq", "gelu_tanh_approx"] = None,
    cu_seqlens_m: Optional[Tensor] = None,
    A_idx: Optional[Tensor] = None,  # (total_M,) if gather_A with varlen_m
    out_dtype: Optional[torch.dtype] = None,
    postact_dtype: Optional[torch.dtype] = None,
    store_preact: bool = True,
) -> Tuple[Optional[Tensor], Tensor]:
    out_dtype = A.dtype if out_dtype is None else out_dtype
    postact_dtype = A.dtype if postact_dtype is None else postact_dtype
    if C is None:
        out = gemm_ref(A, B, cu_seqlens_m=cu_seqlens_m, A_idx=A_idx)
    else:
        out = gemm_add_ref(A, B, C, cu_seqlens_m=cu_seqlens_m, A_idx=A_idx)
    postact = act_to_pytorch_fn_map[activation](out).to(postact_dtype)
    return out.to(out_dtype) if store_preact else None, postact


def gemm_dact(
    A: Tensor,  # (M, K) or (L, M, K) or (total_M, K) if varlen_m or (whatever, K) if gather_A with varlen_m
    B: Tensor,  # (K, N) or (L, K, N)
    PreAct: Tensor,  # (M, N) or (L, M, N) or (total_M, N) if varlen_m
    activation: Literal[None, "relu", "relu_sq", "gelu_tanh_approx"] = None,
    dx_out: Optional[Tensor] = None,  # (M, N) or (L, M, N) or (total_M, N) if varlen_m
    postact_out: Optional[Tensor] = None,  # (M, N) or (L, M, N) or (total_M, N) if varlen_m
    out_dtype: Optional[torch.dtype] = None,
    postact_dtype: Optional[torch.dtype] = None,
    cu_seqlens_m: Optional[Tensor] = None,
    A_idx: Optional[Tensor] = None,  # (total_M,) if gather_A with varlen_m
    dynamic_scheduler: bool = True,
    tuned: bool = True,
) -> Tuple[Tensor, Tensor]:
    """GEMM with activation gradient and optional output tensors."""
    out_dtype = A.dtype if out_dtype is None else out_dtype
    postact_dtype = PreAct.dtype if postact_dtype is None else postact_dtype
    varlen_m = cu_seqlens_m is not None
    # Determine output shape based on gather_A
    if varlen_m:
        total_m = A_idx.shape[0] if A_idx is not None else A.shape[0]
        out_shape = (total_m, B.shape[-1])
    elif A.ndim == 2:
        out_shape = (A.shape[0], B.shape[-1])
    else:
        out_shape = (A.shape[0], A.shape[-2], B.shape[-1])
    if dx_out is None:
        dx_out = torch.empty(out_shape, dtype=out_dtype, device=A.device)
    if postact_out is None:
        postact_out = torch.empty(out_shape, dtype=postact_dtype, device=A.device)
    gemm_dact_out(
        A, B, PreAct, dx_out, postact_out, activation, cu_seqlens_m, A_idx, dynamic_scheduler, tuned
    )
    return dx_out, postact_out


@torch.library.custom_op(
    "quack::gemm_dact_out",
    mutates_args=("dx_out", "postact_out"),
    device_types="cuda",
    schema="(Tensor A, Tensor B, Tensor PreAct, Tensor(a3!) dx_out, Tensor(a4!) postact_out, str? activation=None, Tensor? cu_seqlens_m=None, Tensor? A_idx=None, bool dynamic_scheduler=True, bool tuned=True) -> ()",
)
def gemm_dact_out(
    A: Tensor,  # (M, K) or (L, M, K) or (total_M, K) if varlen_m or (whatever, K) if gather_A with varlen_m
    B: Tensor,  # (K, N) or (L, K, N)
    PreAct: Tensor,  # (M, N) or (L, M, N) or (total_M, N) if varlen_m
    dx_out: Tensor,  # (M, N) or (L, M, N) or (total_M, N) if varlen_m
    postact_out: Tensor,  # (M, N) or (L, M, N) or (total_M, N) if varlen_m
    activation: Literal[None, "relu", "relu_sq", "gelu_tanh_approx"] = None,
    cu_seqlens_m: Optional[Tensor] = None,
    A_idx: Optional[Tensor] = None,  # (total_M,) if gather_A with varlen_m
    dynamic_scheduler: bool = True,
    tuned: bool = True,
) -> None:
    """GEMM with activation gradient and pre-allocated output tensors."""
    fn = gemm_dact_tuned if tuned else partial(gemm_dact_tuned.fn, config=None)
    fn(A, B, PreAct, dx_out, postact_out, activation, cu_seqlens_m, A_idx, dynamic_scheduler)


def gemm_dact_ref(
    A: Tensor,  # (M, K) or (L, M, K) or (total_M, K) if varlen_m or (M, total_K) if varlen_k or (whatever, K) if gather_A
    B: Tensor,  # (K, N) or (L, K, N) or (total_K, N) if varlen_k
    PreAct: Tensor,  # (M, N) or (L, M, N) or (total_M, N) if varlen_m
    activation: Literal[None, "relu", "relu_sq", "gelu_tanh_approx"] = None,
    cu_seqlens_m: Optional[Tensor] = None,
    A_idx: Optional[Tensor] = None,  # (total_M,) if gather_A with varlen_m
    out_dtype: Optional[torch.dtype] = None,
    postact_dtype: Optional[torch.dtype] = None,
) -> Tuple[Tensor, Tensor]:
    """Reference implementation for GEMM with activation gradient."""
    out_dtype = A.dtype if out_dtype is None else out_dtype
    postact_dtype = PreAct.dtype if postact_dtype is None else postact_dtype
    dout = gemm_ref(A, B, cu_seqlens_m=cu_seqlens_m, A_idx=A_idx).to(out_dtype)
    postact = act_to_pytorch_fn_map[activation](PreAct)
    # Compute gradient using autograd
    if activation is None:
        dx = dout
    else:
        PreAct_requires_grad = PreAct.requires_grad
        PreAct.requires_grad_(True)
        postact_for_grad = act_to_pytorch_fn_map[activation](PreAct)
        dx = torch.autograd.grad(postact_for_grad, PreAct, dout, create_graph=False)[0]
        PreAct.requires_grad_(PreAct_requires_grad)
    return dx.to(out_dtype), postact.to(postact_dtype)


def gemm_gated_ref(
    A: Tensor,  # (M, K) or (L, M, K) or (total_M, K) if varlen_m or (M, total_K) if varlen_k or (whatever, K) if gather_A
    B: Tensor,  # (K, N) or (L, K, N) or (total_K, N) if varlen_k
    C: Optional[Tensor] = None,  # (M, N) or (L, M, N) or (total_M, N) if varlen_m
    activation: Literal["glu", "swiglu", "swiglu_oai", "reglu", "geglu"] = "swiglu",
    cu_seqlens_m: Optional[Tensor] = None,
    A_idx: Optional[Tensor] = None,  # (total_M,) if gather_A with varlen_m
    out_dtype: Optional[torch.dtype] = None,
    postact_dtype: Optional[torch.dtype] = None,
    store_preact: bool = True,
) -> Tuple[Optional[Tensor], Tensor]:
    """Reference implementation for GEMM with gated activation forward.

    Args:
        A: (M, K) - input tensor
        B: (K, N) - weight tensor with gate and up projections
        C: (M, N) - optional bias tensor
        activation: Type of gated activation
        out_dtype: Output dtype for preact
        postact_dtype: Output dtype for postact
        store_preact: Whether to return the pre-activation

    Returns:
        (preact, postact) where:
        - preact: (M, N) pre-activation (if store_preact=True, else None)
        - postact: (M, N // 2) post-activation output
    """
    out_dtype = A.dtype if out_dtype is None else out_dtype
    postact_dtype = A.dtype if postact_dtype is None else postact_dtype
    if C is None:
        preact = gemm_ref(A, B, cu_seqlens_m=cu_seqlens_m, A_idx=A_idx)
    else:
        preact = gemm_add_ref(A, B, C, cu_seqlens_m=cu_seqlens_m, A_idx=A_idx)
    # Split preact into gate and up projections
    gate = preact[..., ::2]  # (M, N//2)
    up = preact[..., 1::2]  # (M, N//2)
    postact = gated_to_pytorch_fn_map[activation](gate, up)
    return preact.to(out_dtype) if store_preact else None, postact.to(postact_dtype)


def gemm_dgated_ref(
    A: Tensor,  # (M, K) or (L, M, K) or (total_M, K) if varlen_m or (M, total_K) if varlen_k or (whatever, K) if gather_A
    B: Tensor,  # (K, N) or (L, K, N) or (total_K, N) if varlen_k
    PreAct: Tensor,  # (M, 2*N) or (L, M, 2*N) or (total_M, 2*N) if varlen_m
    activation: Literal["glu", "swiglu", "swiglu_oai", "reglu", "geglu"],
    cu_seqlens_m: Optional[Tensor] = None,
    A_idx: Optional[Tensor] = None,  # (total_M,) if gather_A with varlen_m
    out_dtype: Optional[torch.dtype] = None,
    postact_dtype: Optional[torch.dtype] = None,
) -> Tuple[Tensor, Tensor]:
    """Reference implementation for GEMM with gated activation gradient.

    Args:
        A: (M, K) - dout input tensor
        B: (K, N) - weight tensor
        PreAct: (M, 2*N) - pre-activation tensor with gate and up projections interleaved
        activation: Type of gated activation
        out_dtype: Output dtype for dx
        postact_dtype: Output dtype for postact

    Returns:
        (dx, postact) where:
        - dx: (M, 2*N) gradient w.r.t. PreAct
        - postact: (M, N) post-activation output
    """
    out_dtype = A.dtype if out_dtype is None else out_dtype
    postact_dtype = PreAct.dtype if postact_dtype is None else postact_dtype
    dout = gemm_ref(A, B, cu_seqlens_m=cu_seqlens_m, A_idx=A_idx).to(out_dtype)
    # Split PreAct into gate and up projections
    gate = PreAct[..., ::2]  # (M, N)
    up = PreAct[..., 1::2]  # (M, N)
    postact = gated_to_pytorch_fn_map[activation](gate, up)
    # Use autograd to compute gradients w.r.t. gate and up
    dgate, dup = torch.autograd.grad(postact, [gate, up], dout, create_graph=False)
    # Interleave gradients back
    dx = torch.stack([dgate, dup], dim=-1).reshape(PreAct.shape)
    return dx.to(out_dtype), postact.to(postact_dtype)


# TODO: this is not quite right, do we need to register gemm_add not gemm_add_out?
# try:
#     from torch._inductor.fx_passes.reinplace import InplaceableOp
#     torch._inductor.fx_passes.reinplace.inplaceable_ops.update({
#         torch.ops.quack.gemm_add_out.default:
#         InplaceableOp(torch.ops.quack.gemm_add_inplace.default, mutated_arg=2)
#     })
# except ImportError:
#     pass

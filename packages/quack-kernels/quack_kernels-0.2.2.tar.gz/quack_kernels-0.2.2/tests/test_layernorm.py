# tests/test_layernorm.py

import pytest
import torch

from quack.layernorm import layernorm, layernorm_ref, rstd_ref, mean_ref


@pytest.mark.parametrize("eps", [1e-5, 1e-6])
@pytest.mark.parametrize("input_dtype", [torch.bfloat16, torch.float16, torch.float32])
@pytest.mark.parametrize("M", [1, 37, 199])
@pytest.mark.parametrize(
    "N", [256, 512, 760, 1024, 1128, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144]
)  # , 32768])
def test_layernorm_forward(M, N, input_dtype, eps):
    """Test LayerNorm forward pass against reference implementation."""
    device = "cuda"

    # tolerance depends on precision
    if input_dtype == torch.bfloat16:
        atol = 1e-2
        rtol = 1e-2
    elif input_dtype == torch.float16:
        atol = 1e-3
        rtol = 1e-3
    else:
        atol = 1e-4
        rtol = 1e-4

    torch.random.manual_seed(0)
    x = torch.randn(M, N, device=device, dtype=input_dtype, requires_grad=True)
    weight = torch.randn(N, device=device, dtype=torch.float32, requires_grad=True)

    # pure‐PyTorch refs
    x_ref = x.detach().clone().requires_grad_()
    weight_ref = weight.detach().clone().requires_grad_()

    out, rstd, mean = layernorm(x, weight, eps=eps, return_rstd=True, return_mean=True)
    out_ref = layernorm_ref(x_ref, weight_ref, eps=eps)
    rstd_ref_val = rstd_ref(x_ref, eps=eps)
    mean_ref_val = mean_ref(x_ref)

    # shapes & dtypes
    assert out.shape == x.shape
    assert out.dtype == input_dtype
    assert rstd.shape == (M,) and rstd.dtype == torch.float32
    assert mean.shape == (M,) and mean.dtype == torch.float32

    # numeric check
    torch.testing.assert_close(out, out_ref, atol=atol, rtol=rtol)
    torch.testing.assert_close(rstd, rstd_ref_val, atol=6e-4, rtol=6e-4)
    torch.testing.assert_close(mean, mean_ref_val, atol=6e-4, rtol=6e-4)


@pytest.mark.parametrize("return_rstd", [True, False])
@pytest.mark.parametrize("return_mean", [True, False])
def test_layernormnorm_return_rstd_option(return_rstd, return_mean):
    """Test that return_rstd option works correctly."""
    device = "cuda"
    M, N = 32, 1024
    eps = 1e-6

    x = torch.randn(M, N, device=device, dtype=torch.float16)
    weight = torch.randn(N, device=device, dtype=torch.float32)

    if return_rstd and return_mean:
        out, rstd, mean = layernorm(x, weight, eps=eps, return_rstd=True, return_mean=True)
        assert out.shape == (M, N)
        assert rstd.shape == (M,)
        assert rstd.dtype == torch.float32
        assert mean.shape == (M,)
        assert mean.dtype == torch.float32
    elif return_rstd and not return_mean:
        out, rstd = layernorm(x, weight, eps=eps, return_rstd=True, return_mean=False)
        assert out.shape == (M, N)
        assert rstd.shape == (M,)
        assert rstd.dtype == torch.float32
    elif not return_rstd and return_mean:
        out, mean = layernorm(x, weight, eps=eps, return_rstd=False, return_mean=True)
        assert out.shape == (M, N)
        assert mean.shape == (M,)
        assert mean.dtype == torch.float32
    else:
        out = layernorm(x, weight, eps=eps, return_rstd=False, return_mean=False)
        assert out.shape == (M, N)
        assert isinstance(out, torch.Tensor)


def test_layernorm_input_validation():
    """Test input validation and error handling."""
    device = "cuda"

    # Test 3D input (should fail)
    x_3d = torch.randn(2, 32, 1024, device=device, dtype=torch.float16)
    weight = torch.randn(1024, device=device, dtype=torch.float32)

    with pytest.raises(AssertionError, match="Input must be 2D"):
        layernorm(x_3d, weight)

    # Test weight dimension mismatch
    x = torch.randn(32, 1024, device=device, dtype=torch.float16)
    weight_wrong = torch.randn(512, device=device, dtype=torch.float32)

    with pytest.raises(AssertionError, match="Last dimension of input must match weight dimension"):
        layernorm(x, weight_wrong)

    # Test CPU tensors (should fail)
    x_cpu = torch.randn(32, 1024, dtype=torch.float16)
    weight_cpu = torch.randn(1024, dtype=torch.float32)

    with pytest.raises(AssertionError, match="Tensors must be on CUDA device"):
        layernorm(x_cpu, weight_cpu)

    # Test unsupported dtype
    x = torch.randn(32, 1024, device=device, dtype=torch.float64)
    weight = torch.randn(1024, device=device, dtype=torch.float32)

    with pytest.raises(AssertionError, match="Unsupported dtype"):
        layernorm(x, weight)

    # Test wrong weight dtype
    x = torch.randn(32, 1024, device=device, dtype=torch.float16)
    weight_wrong_dtype = torch.randn(1024, device=device, dtype=torch.float16)

    with pytest.raises(AssertionError, match="Weight must be float32"):
        layernorm(x, weight_wrong_dtype)


def test_layernorm_compile_cache():
    """Test that compile cache works correctly for repeated calls."""
    device = "cuda"
    M, N = 32, 1024
    eps = 1e-6

    # Clear cache
    layernorm.compile_cache.clear()
    assert len(layernorm.compile_cache) == 0

    x1 = torch.randn(M, N, device=device, dtype=torch.float16)
    weight1 = torch.randn(N, device=device, dtype=torch.float32)

    # First call should compile
    out1 = layernorm(x1, weight1, eps=eps)
    assert len(layernorm.compile_cache) == 1

    # Same shape should reuse cache
    x2 = torch.randn(M, N, device=device, dtype=torch.float16)
    weight2 = torch.randn(N, device=device, dtype=torch.float32)
    out2 = layernorm(x2, weight2, eps=eps)
    assert len(layernorm.compile_cache) == 1

    # Different shape should create new cache entry
    x3 = torch.randn(M, N * 2, device=device, dtype=torch.float16)
    weight3 = torch.randn(N * 2, device=device, dtype=torch.float32)
    out3 = layernorm(x3, weight3, eps=eps)
    assert len(layernorm.compile_cache) == 2

    # Different dtype should create new cache entry
    x4 = torch.randn(M, N, device=device, dtype=torch.float32)
    weight4 = torch.randn(N, device=device, dtype=torch.float32)
    out4 = layernorm(x4, weight4, eps=eps)
    assert len(layernorm.compile_cache) == 3

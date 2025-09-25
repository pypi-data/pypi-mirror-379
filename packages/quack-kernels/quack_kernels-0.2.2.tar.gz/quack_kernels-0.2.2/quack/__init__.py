__version__ = "0.2.2"

import cutlass.cute as cute

from quack.rmsnorm import rmsnorm
from quack.softmax import softmax
from quack.cross_entropy import cross_entropy

import quack.cute_dsl_utils

# Patch cute.compile to optionally dump SASS
cute.compile = quack.cute_dsl_utils.cute_compile_patched

__all__ = [
    "rmsnorm",
    "softmax",
    "cross_entropy",
]

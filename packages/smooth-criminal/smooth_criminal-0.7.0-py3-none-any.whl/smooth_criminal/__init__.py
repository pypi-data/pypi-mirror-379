"""Paquete principal de Smooth Criminal."""

__version__ = "0.5.0"

from .core import (
    smooth,
    vectorized,
    guvectorized,
    moonwalk,
    thriller,
    jam,
    black_or_white,
    beat_it,
    bad,
    dangerous,
    bad_and_dangerous,
    profile_it,
    mj_mode,
)

from .benchmark import benchmark_jam, detect_fastest_backend

__all__ = [
    "smooth",
    "vectorized",
    "guvectorized",
    "moonwalk",
    "thriller",
    "jam",
    "black_or_white",
    "beat_it",
    "bad",
    "dangerous",
    "bad_and_dangerous",
    "profile_it",
    "mj_mode",
    "benchmark_jam",
    "detect_fastest_backend",
    "__version__",
]

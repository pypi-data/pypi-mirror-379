"""Utilities to benchmark ``jam`` backends.

This module provides :func:`benchmark_jam` to measure execution time of a
function across the available ``jam`` backends (``thread``, ``process`` and
``async``).  It also exposes :func:`detect_fastest_backend` which runs the
benchmark and returns the fastest backend.
"""

from __future__ import annotations

import asyncio
import time
from typing import Any, Callable, Dict, List, Sequence

from .core import jam

Backends = Sequence[str]


def benchmark_jam(
    func: Callable[[Any], Any], args: Sequence[Any], backends: Backends
) -> Dict[str, Any]:
    """Benchmark ``func`` using ``jam`` with different backends.

    Parameters
    ----------
    func:
        Function to execute. It must be importable at module level so the
        ``process`` backend can pickle it.
    args:
        Sequence of arguments that will be fed to the function.
    backends:
        Iterable with backend names (``thread``, ``process`` or ``async``).

    Returns
    -------
    dict
        A dictionary containing a ``metrics`` list with timing information for
        each backend and the name of the ``fastest`` backend.
    """

    metrics: List[Dict[str, Any]] = []
    for backend in backends:
        metric: Dict[str, Any] = {"backend": backend, "success": False}
        wrapped = jam(workers=len(args), backend=backend)(func)
        start = time.perf_counter()
        try:
            if backend == "async":
                asyncio.run(wrapped(args))
            else:
                wrapped(args)
        except Exception as exc:  # pragma: no cover - surfaces in tests
            metric["error"] = str(exc)
        else:
            end = time.perf_counter()
            metric.update({"duration": end - start, "success": True})
        metrics.append(metric)

    successful = [m for m in metrics if m.get("success")]
    fastest = (
        min(successful, key=lambda m: m["duration"])["backend"]
        if successful
        else None
    )
    return {"metrics": metrics, "fastest": fastest}


def detect_fastest_backend(
    func: Callable[[Any], Any], args: Sequence[Any], backends: Backends
) -> str:
    """Return the fastest backend for ``func`` over ``args``.

    This is a thin wrapper over :func:`benchmark_jam` that extracts the name of
    the backend with the lowest duration.
    """

    result = benchmark_jam(func, args, backends)
    return str(result["fastest"])


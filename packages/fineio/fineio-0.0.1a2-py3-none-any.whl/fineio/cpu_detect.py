# cpu_detect.py
import time
from typing import Callable, Any

_CPU_HEAVY_CACHE = {}
CPU_HEAVY_THRESHOLD = 0.001  # 1 ms

def is_cpu_heavy(func: Callable, *args, **kwargs) -> bool:
    """Detect if a sync function is CPU-heavy."""
    key = (func, args, tuple(kwargs.items()))
    if key in _CPU_HEAVY_CACHE:
        return _CPU_HEAVY_CACHE[key]

    start = time.perf_counter()
    func(*args, **kwargs)
    duration = time.perf_counter() - start

    is_heavy = duration > CPU_HEAVY_THRESHOLD
    _CPU_HEAVY_CACHE[key] = is_heavy
    return is_heavy

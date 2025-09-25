# executor.py
import asyncio
from concurrent.futures import ProcessPoolExecutor
import os
from typing import Callable, Any, Union
from .cpu_detect import is_cpu_heavy

CPU_CORES = os.cpu_count() or 1
POOL = ProcessPoolExecutor(max_workers=CPU_CORES)

def _run_sync(func: Callable, *args, **kwargs) -> Any:
    return func(*args, **kwargs)

async def _run_async(func: Callable, *args, **kwargs) -> Any:
    if asyncio.iscoroutinefunction(func):
        return await func(*args, **kwargs)
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(POOL, func, *args, **kwargs)

def run(func: Callable, *args, **kwargs) -> Union[Any, asyncio.Future]:
    """
    Execute function efficiently:
    - auto detects CPU-heavy tasks
    - zero-overhead for trivial sync
    - async-aware
    """
    try:
        loop = asyncio.get_running_loop()
        in_async = True
    except RuntimeError:
        in_async = False

    if in_async:
        if not asyncio.iscoroutinefunction(func) and is_cpu_heavy(func, *args, **kwargs):
            return loop.run_in_executor(POOL, func, *args, **kwargs)
        return _run_async(func, *args, **kwargs)
    else:
        if not asyncio.iscoroutinefunction(func) and is_cpu_heavy(func, *args, **kwargs):
            return POOL.submit(func, *args, **kwargs).result()
        return _run_sync(func, *args, **kwargs)

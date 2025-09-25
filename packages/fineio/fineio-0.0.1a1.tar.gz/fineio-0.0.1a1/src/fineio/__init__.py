import asyncio
from typing import Union

__version__ = "0.0.1a1"

async def _hello_async() -> str:
    return "fineio is alive!"

def hello() -> Union[str, asyncio.Future]:
    """
    Can be used in both sync and async code.

    Sync:   result = hello()
    Async:  result = await hello()
    """
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        # No loop → we're in sync context
        return asyncio.run(_hello_async())
    else:
        # Inside running loop → return coroutine
        return _hello_async()

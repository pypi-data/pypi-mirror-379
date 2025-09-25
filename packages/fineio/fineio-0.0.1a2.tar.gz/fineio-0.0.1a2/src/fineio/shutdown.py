# shutdown.py
from .executor import POOL

def shutdown():
    """Shutdown the process pool."""
    POOL.shutdown(wait=True)

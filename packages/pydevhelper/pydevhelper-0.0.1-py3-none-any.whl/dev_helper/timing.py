import time
import functools
import logging

def timer(func):
    """Decorator to measure execution time of functions."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        logging.info(f"Function '{func.__name__}' executed in {elapsed:.4f}s")
        return result

    return wrapper

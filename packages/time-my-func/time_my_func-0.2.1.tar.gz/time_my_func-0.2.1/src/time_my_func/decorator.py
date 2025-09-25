import functools
import inspect
import time

# Global toggle
ENABLED = True


def set_enabled(value: bool = True):
    """
    Globally enable or disable all @timeit() decorators.

    When disabled, @timeit() will not measure or print execution times,
    and functions will execute normally with minimal overhead.

    Args:
        value (bool): 
            True to enable timing, False to disable.
    
    Example:
        >>> from timeitdecorator import set_enabled
        >>> set_enabled(False)  # Disable all timing
        >>> set_enabled(True)   # Re-enable timing
    """
    global ENABLED
    ENABLED = value

def timeit(decimals: int = 3, unit: str = "auto"):
    """
    Decorator to print execution time of a function, robust to exceptions and supports async.

    Args:
        decimals (int): Number of decimal places in output (default=3).
        unit (str): Unit to display. Options: "ns", "us", "µs", "ms", "s", "m", "auto".
    """

    valid_units = {"ns", "us", "µs", "ms", "s", "m", "auto"}
    if unit not in valid_units:
        raise ValueError(f"Invalid unit '{unit}'. Choose from {valid_units}.")

    def decorator(func):
        if inspect.iscoroutinefunction(func):
            # Async version
            @functools.wraps(func)
            async def async_wrapper(*args, **kwargs):
                if not ENABLED:
                    return func(*args, **kwargs)
                start = time.perf_counter_ns()
                try:
                    return await func(*args, **kwargs)
                finally:
                    end = time.perf_counter_ns()
                    elapsed_ns = end - start
                    display_time, display_unit = _format_time(elapsed_ns, decimals, unit)
                    try:
                        print(f"[{func.__name__}] Execution time: {display_time} {display_unit}")
                    except Exception:
                        pass  # Fail silently if print fails
            return async_wrapper
        else:
            # Synchronous version
            @functools.wraps(func)
            def sync_wrapper(*args, **kwargs):
                if not ENABLED:
                    return func(*args, **kwargs)
                start = time.perf_counter_ns()
                try:
                    return func(*args, **kwargs)
                finally:
                    end = time.perf_counter_ns()
                    elapsed_ns = end - start
                    display_time, display_unit = _format_time(elapsed_ns, decimals, unit)
                    try:
                        print(f"[{func.__name__}] Execution time: {display_time} {display_unit}")
                    except Exception:
                        pass
            return sync_wrapper

    return decorator


def _format_time(elapsed_ns: int, decimals: int, unit: str):
    """Format nanoseconds into best-fitting unit or a forced unit."""
    conversions = {
        "ns": 1,
        "µs": 1_000,
        "us": 1_000,  # alias
        "ms": 1_000_000,
        "s": 1_000_000_000,
        "m": 60_000_000_000,
    }

    if unit == "auto":
        if elapsed_ns < conversions["µs"]:
            unit = "ns"
        elif elapsed_ns < conversions["ms"]:
            unit = "µs"
        elif elapsed_ns < conversions["s"]:
            unit = "ms"
        elif elapsed_ns < conversions["m"]:
            unit = "s"
        else:
            unit = "m"

    if unit not in conversions:
        raise ValueError(f"Unsupported unit: {unit}")

    value = elapsed_ns / conversions[unit]
    formatted = f"{value:.{decimals}f}"
    return formatted, "µs" if unit == "us" else unit

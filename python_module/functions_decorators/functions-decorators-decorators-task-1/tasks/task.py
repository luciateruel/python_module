from typing import Dict
import time
execution_time: Dict[str, float] = {}
from time import sleep


def time_decorator(fn):
    """
    Create a decorator function `time_decorator`
    which has to calculate decorated function execution time
    and put this time value to `execution_time` dictionary where `key` is
    decorated function name and `value` is this function execution time.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()

        result = fn(*args, **kwargs)

        end_time = time.time()

        execution_time[fn.__name__] = end_time - start_time
        return result
    return wrapper



@time_decorator
def func_add(a, b):
    sleep(0.2)
    return a + b

print(func_add(10, 20))
# 30

print(execution_time['func_add'])
# 0.212341254

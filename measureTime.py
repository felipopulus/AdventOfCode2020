from functools import wraps
from time import time


def measure_time(func):
    @wraps(func)
    def _time_it(*args, **kwargs):
        start = int(round(time() * 1000))
        try:
            return func(*args, **kwargs)
        finally:
            end_ = int(round(time() * 1000)) - start
            print("Total execution time: {} ms".format(end_ if end_ > 0 else 0))
    return _time_it

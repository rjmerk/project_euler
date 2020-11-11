import time
from contextlib import contextmanager


@contextmanager
def measure_execution_time():
    t1 = time.time()
    yield
    t2 = time.time() - t1
    print("Time in milliseconds: {:10.2f}".format(t2 * 1000))

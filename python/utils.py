import time
from contextlib import contextmanager


@contextmanager
def measure_execution_time(message="Time in milliseconds"):
    t1 = time.time()
    yield
    t2 = time.time() - t1
    print(f"{message}: {t2 * 1000:10.2f}")

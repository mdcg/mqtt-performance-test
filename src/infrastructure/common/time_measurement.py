from time import perf_counter
from typing import Callable


class TimeMeasurement:
    def __enter__(self) -> Callable[[], float]:
        self.start = perf_counter()
        self.end = 0.0
        return lambda: self.end - self.start

    def __exit__(self, *args):
        self.end = perf_counter()

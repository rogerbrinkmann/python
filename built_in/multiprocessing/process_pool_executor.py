import time
from math import sin
from concurrent.futures import ProcessPoolExecutor, as_completed


def process_function(num):
    """
    just a cpu heavy function
    """
    start = time.perf_counter()
    sum([sin(i) for i in range(num)])
    return time.perf_counter() - start


if __name__ == "__main__":
    start = time.perf_counter()
    sum_durations = 0
    # context manager manages joining processes
    with ProcessPoolExecutor() as executor:
        numbers = [1000000 for i in range(30)]
        durations = executor.map(process_function, numbers)

        for duration in durations:
            print(f"{duration:0.3f}")   
            sum_durations += duration

    print(f"Time actual: {time.perf_counter() - start:0.3f}s")
    print(f"Sum time individual: {sum_durations:0.3f}")

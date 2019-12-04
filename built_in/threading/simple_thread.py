"""
Simple script to demonstrate starting of simple threads
"""
from threading import Thread, current_thread
import time
from math import factorial

CPU_BOUND = True
IO_BOUND = False


def wait(time_to_wait):
    """
    simulate a cpu - heavy task by calculating factorial
    """
    for i in range(time_to_wait):
        print(f"{current_thread().name} - {i}")
        if CPU_BOUND:
            factorial(100000)
        if IO_BOUND:
            time.sleep(0.5)


def function(time_to_wait):
    print(f"{current_thread().name} start")
    wait(time_to_wait)
    print(f"{current_thread().name} end")


def main():
    start = time.perf_counter()

    threads = []
    for thread in range(10):
        thread = Thread(target=function, args=(10,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    end = time.perf_counter()

    print(f"Duration: {end-start}")


if __name__ == "__main__":
    main()

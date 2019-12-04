"""
Simple script to demonstrate starting of simple processes
"""
import time
from math import factorial
from multiprocessing import Process, current_process

CPU_BOUND = True
IO_BOUND = False


def wait(time_to_wait):
    """
    simulate a cpu - heavy task by calculating factorial
    """
    for i in range(time_to_wait):
        print(f"{current_process().name} - {i}")
        if CPU_BOUND:
            factorial(100000)
        if IO_BOUND:
            time.sleep(0.5)


def function(time_to_wait):
    print(f"{current_process().name} start")
    wait(time_to_wait)
    print(f"{current_process().name} end")


def main():
    start = time.perf_counter()

    processes = []
    for process in range(10):
        process = Process(target=function, args=(10,))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    end = time.perf_counter()

    print(f"Duration: {end-start}")


if __name__ == "__main__":
    main()

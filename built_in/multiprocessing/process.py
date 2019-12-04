import time
from math import sin
from multiprocessing import Process, current_process


def process_function(num):
    """
    just a cpu heavy function
    """
    start = time.perf_counter()
    sum([sin(i) for i in range(num)])
    print(f"Process {current_process().pid}: {time.perf_counter() - start:0.3f}s")


if __name__ == "__main__":
    start = time.perf_counter()
    processes = []
    for process in range(10):
        process = Process(target=process_function, args=(1000000, ))
        process.start()
        processes.append(process)
    
    for process in processes:
        process.join()
    
    print(f"Total: {time.perf_counter() - start:0.3f}s")


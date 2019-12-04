import os
import time
from multiprocessing import Pool


def f(x):
    print(os.getpid())
    a = sum([i ** i for i in range(x)])/x
    return a


if __name__ == "__main__":
    with Pool(10) as p:
        print(p.map(f, [10, 10,10]))

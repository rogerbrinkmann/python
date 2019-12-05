import time
from math import factorial


def test_gen(num):
    start = time.perf_counter()

    gen = (factorial(1000) for i in range(num))

    mid = time.perf_counter()

    for g in gen:
        a = g

    end = time.perf_counter()
    return start, mid, end


def test_list(num):
    start = time.perf_counter()

    lst = [factorial(1000) for i in range(num)]

    mid = time.perf_counter()

    for l in lst:
        a = l

    end = time.perf_counter()
    return start, mid, end


gen_start, gen_mid, gen_end = test_gen(10000)
lst_start, lst_mid, lst_end = test_list(10000)


print(f"Generator Setup:      {gen_mid-gen_start:10.8f}")
print(f"List Setup:           {lst_mid-lst_start:10.8f}")
print()
print(f"Generator Consumtion: {gen_end-gen_mid:10.8f}")
print(f"List Consumtion:      {lst_end-lst_mid:10.8f}")
print()
print(f"Generator Total:      {gen_end-gen_start:10.8f}")
print(f"List Total:           {lst_end-lst_start:10.8f}")


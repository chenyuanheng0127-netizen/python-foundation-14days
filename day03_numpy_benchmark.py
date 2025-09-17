import time
import numpy as np

def python_listcomp(nums):
    return [x * x for x in nums]

def python_square_loop(nums):
    result = []
    for x in nums:
        result.append(x * x)
    return result

def numpy_square(arr):
    return arr * arr

def benchmark(N):
    nums = list(range(N))
    arr = np.arange(N)

    t0 = time.perf_counter()
    _ = python_listcomp(nums)
    t1 = time.perf_counter()

    t2 = time.perf_counter()
    _ = python_square_loop(nums)
    t3 = time.perf_counter()

    t4 = time.perf_counter()
    _ = numpy_square(arr)
    t5 = time.perf_counter()

    print(f"N={N:>8}  python listcomp: {t1 - t0:.6f}s  |  python loop: {t3 - t2:.6f}s  | numpy: {t5 - t4:.6f}s")

if __name__ == "__main__":
    for size in [10, 1000, 10_000, 100_000, 1_000_000]:
        benchmark(size)
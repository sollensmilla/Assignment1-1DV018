"""
This file contains the experiments for part 1. It will generate a
list of random integers and then run all the algorithms from
threesum.py.
"""
import time
import math
from threesum import generate_list, threesum_brute, threesum_pointer


def test_correctness():
    for run in range(3):
        lst = generate_list(15)
        result_brute = threesum_brute(lst)
        result_pointer = threesum_pointer(lst)

        print(f"Run {run + 1}")
        print(f"Input: {lst}")
        print(f"Brute result: {result_brute}")
        print(f"Pointer result: {result_pointer}")
        print()


def logspace_sizes(n_min, n_max, count):
    log_min = math.log2(n_min)
    log_max = math.log2(n_max)
    step = (log_max - log_min) / (count -1)

    sizes = []
    for i in range(count):
        log_val = log_min + i * step
        sizes.append(round(2 ** log_val))

    return sorted(set(sizes))


def time_brute():
    for n in [250, 350, 450, 600, 700, 900]:
        lst = generate_list(n)
        start = time.perf_counter()
        threesum_brute(lst)
        elapsed = time.perf_counter() - start
        print(f"n={n}: {elapsed:.3f} seconds")


def time_pointer():
    for n in [2000, 3000, 4000, 5000, 9000, 12000]:
        lst = generate_list(n)
        start = time.perf_counter()
        threesum_pointer(lst)
        elapsed = time.perf_counter() - start
        print(f"n={n}: {elapsed:.3f} seconds")       


def main():
    print("=== Test correctness ===")
    test_correctness()

    print("=== Threesum brute ===")
    time_brute()

    print("=== Threesum pointer ===")
    time_pointer()

    print(f"Logspace sizes for brute: {logspace_sizes(250, 900, 15)}")
    print(f"Logspace sizes for pointer: {logspace_sizes(2000, 12000, 15)}")


if __name__ == "__main__":
    main()

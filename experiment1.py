"""
This file contains the experiments for part 1. It will generate a
list of random integers and then run all the algorithms from
threesum.py.
"""
import time
import math
import matplotlib.pyplot as plt
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
    step = (log_max - log_min) / (count - 1)

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


def run_experiment(sizes, func, num_runs=3):
    times = []

    for run in range(num_runs):
        run_times = []
        for n in sizes:
            lst = generate_list(n)
            start = time.perf_counter()
            func(lst)
            elapsed = time.perf_counter() - start
            run_times.append(elapsed)
        times.append(run_times)

    return times


def plot_runs(sizes, times, title):
    plt.figure()
    for i, run_times in enumerate(times):
        plt.plot(sizes, run_times, marker='o', label=f"Run {i + 1}")

    plt.xlabel("List size (n)")
    plt.ylabel("Time (seconds)")
    plt.title(title)
    plt.legend()
    plt.show()


def average_times(times):
    result = []
    for vals in zip(*times):
        avg = sum(vals) / len(vals)
        result.append(avg)
    return result


def plot_average(sizes, avg_times, title):
    plt.figure()
    plt.plot(sizes, avg_times, marker='o')
    plt.xlabel("List size (n)")
    plt.ylabel("Average time (seconds)")
    plt.title(title)
    plt.show()


def main():
    print("=== Test correctness ===")
    test_correctness()

    # print("=== Running test to see time complexity of brute ===")
    # time_brute()

    # print("=== Running test to see time complexity of pointer ===")
    # time_pointer()

    brute_sizes = logspace_sizes(250, 900, 15)
    pointer_sizes = logspace_sizes(2000, 12000, 15)
    print(f"Logspace sizes for brute: {brute_sizes}")
    print(f"Logspace sizes for pointer: {pointer_sizes}")

    print("=== Running full experiment for brute ===")
    brute_times = run_experiment(brute_sizes, threesum_brute)
    print(brute_times)

    print("=== Running full experiment for pointer ===")
    pointer_times = run_experiment(pointer_sizes, threesum_pointer)
    print(pointer_times)

    plot_runs(brute_sizes, brute_times, "Figure 1 Brute force: 3 runs")
    plot_runs(pointer_sizes, pointer_times, "Figure 1 Pointer: 3 runs")

    brute_avg = average_times(brute_times)
    pointer_avg = average_times(pointer_times)

    plot_average(brute_sizes, brute_avg, "Figure 1a Brute force: average of 3 runs")
    plot_average(pointer_sizes, pointer_avg, "Figure 1a Pointer: Average of 3 runs")


if __name__ == "__main__":
    main()

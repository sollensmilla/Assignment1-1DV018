"""
This file contains the experiments for part 1. It will generate a
list of random integers and then run all the algorithms from
threesum.py.
"""
import time
from threesum import generate_list, threesum_brute, threesum_pointer
from utils.experiment_utils import (
    logspace_sizes,
    run_experiment,
    average_times,
    estimate_complexity,
    plot_runs,
    plot_averages,
    plot_loglog,
)


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

    # print("=== Running test to see time complexity of brute ===")
    # time_brute()

    # print("=== Running test to see time complexity of pointer ===")
    # time_pointer()

    brute_sizes = logspace_sizes(250, 900, 15)
    pointer_sizes = logspace_sizes(2000, 12000, 15)
    print(f"Logspace sizes for brute: {brute_sizes}")
    print(f"Logspace sizes for pointer: {pointer_sizes}")

    print("=== Running full experiment for brute ===")
    brute_times = run_experiment(brute_sizes, threesum_brute, generate_list)
    print(brute_times)

    print("=== Running full experiment for pointer ===")
    pointer_times = run_experiment(pointer_sizes, threesum_pointer, generate_list)
    print(pointer_times)

    plot_runs(brute_sizes, brute_times, "Figure 1 Brute force: 3 runs")
    plot_runs(pointer_sizes, pointer_times, "Figure 1 Pointer: 3 runs")

    brute_avg = average_times(brute_times)
    pointer_avg = average_times(pointer_times)

    plot_averages(
        brute_sizes, brute_avg, "Figure 1a Brute: average of 3 runs"
    )
    plot_averages(
        pointer_sizes, pointer_avg, "Figure 1a Pointer: Average of 3 runs"
    )

    brute_log_sizes, brute_log_times, brute_m, brute_k = (
        estimate_complexity(brute_sizes, brute_avg, "Brute force")
    )
    pointer_log_sizes, pointer_log_times, pointer_m, pointer_k = (
        estimate_complexity(pointer_sizes, pointer_avg, "Pointer")
    )

    plot_loglog(
        brute_log_sizes, brute_log_times, brute_m, brute_k,
        "Brute force: log-log fit"
    )
    plot_loglog(
        pointer_log_sizes, pointer_log_times, pointer_m, pointer_k,
        "Pointer: log-log fit"
    )


if __name__ == "__main__":
    main()

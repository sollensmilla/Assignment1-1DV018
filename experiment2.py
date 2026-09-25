import time
from quadratic_time_algorithms import (
    generate_random_list,
    selection_sort,
    bubble_sort,
    insertion_sort
)

from n_log_n_algorithms import (
    merge_sort,
    quick_sort
)

from special_case_algorithms import (
    bucket_sort,
    radix_sort
)

from utils.experiment_utils import (
    logspace_sizes,
    run_experiment,
    average_times,
    estimate_complexity,
    plot_comparison,
    plot_loglog_comparison,
)


def test_correctness(sort_func, label, original):
    lst_copy = original.copy()
    result = sort_func(lst_copy)

    print(f"=== {label} ===")
    print(f"Sorted: {result}")
    print(f"Correctly sorted: {result == sorted(original)}")
    print(f"Original unchanged: {lst_copy == original}")


def explore_quadratic_sizes():
    for n in [5000, 8000, 10000, 3000, 12000, 14000]:
        lst = generate_random_list(n)

        start = time.perf_counter()
        selection_sort(lst)
        elapsed = time.perf_counter() - start
        print(f"Selection, n={n}: {elapsed:.3f} seconds")

        start = time.perf_counter()
        bubble_sort(lst)
        elapsed = time.perf_counter() - start
        print(f"Bubble, n={n}: {elapsed:.3f} seconds")

        start = time.perf_counter()
        insertion_sort(lst)
        elapsed = time.perf_counter() - start
        print(f"Insertion, n={n}: {elapsed:.3f} seconds")


def explore_nlogn_sizes():
    for n in [2000000, 2500000, 3000000]:
        lst = generate_random_list(n)

        start = time.perf_counter()
        merge_sort(lst)
        elapsed = time.perf_counter() - start
        print(f"Merge, n={n}: {elapsed:.3f} seconds")

        start = time.perf_counter()
        quick_sort(lst)
        elapsed = time.perf_counter() - start
        print(f"Quick, n={n}: {elapsed:.3f} seconds")


def explore_special_sizes():
    for n in [150000, 1000000, 2300000]:
        lst = generate_random_list(n)

        start = time.perf_counter()
        bucket_sort(lst)
        elapsed = time.perf_counter() - start
        print(f"Bucket, n={n}: {elapsed:.3f} seconds")

        start = time.perf_counter()
        radix_sort(lst)
        elapsed = time.perf_counter() - start
        print(f"Radix, n={n}: {elapsed:.3f} seconds")


def test_all_correctness():
    print("=== Test Correctness ===")
    original = generate_random_list(10)
    print(f"Original: {original}")

    print("=== Quadratic algorithms ===")
    test_correctness(selection_sort, "Selection sort", original)
    test_correctness(bubble_sort, "Bubble sort", original)
    test_correctness(insertion_sort, "Insertion sort", original)

    print("=== N log n algorithms ===")
    test_correctness(merge_sort, "Merge sort", original)
    test_correctness(quick_sort, "Quick sort", original)

    print("=== Special case algorithms ===")
    test_correctness(bucket_sort, "Bucket sort", original)
    test_correctness(radix_sort, "Radix sort", original)


def run_algorithm_experiments(sizes, algorithms):
    avg_times_per_algo = {}
    complexity_per_algo = {}

    for label, func in algorithms.items():
        print(f"=== Running full experiment for {label} ===")
        times = run_experiment(sizes, func, generate_random_list)
        avg_times = average_times(times)
        avg_times_per_algo[label] = avg_times

        log_sizes, log_times, m, k = estimate_complexity(
            sizes, avg_times, label
        )
        complexity_per_algo[label] = (log_times, m, k)

    return avg_times_per_algo, complexity_per_algo, log_sizes


def run_quadratic_experiment():
    sizes = logspace_sizes(3000, 12500, 15)
    print(f"Quadratic sizes: {sizes}")

    algorithms = {
        "Selection sort": selection_sort,
        "Bubble sort": bubble_sort,
        "Insertion sort": insertion_sort
    }

    avg_times, complexity, log_sizes = run_algorithm_experiments(
        sizes, algorithms
    )

    plot_comparison(
        sizes,
        avg_times,
        "Figure: O(n^2) algorithms, average time"
    )

    plot_loglog_comparison(
        log_sizes,
        complexity,
        "Figure: O(n^2) algorithms, log-log fit"
    )


def run_nlogn_experiment():
    sizes = logspace_sizes(150000, 2300000, 15)
    print(f"N log n sizes: {sizes}")

    algorithms = {
        "Merge sort": merge_sort,
        "Quick sort": quick_sort
    }

    avg_times, complexity, log_sizes = run_algorithm_experiments(
        sizes, algorithms
    )

    plot_comparison(
        sizes,
        avg_times,
        "Figure: O(n log n) algorithms, average time"
    )

    plot_loglog_comparison(
        log_sizes,
        complexity,
        "Figure: O(n log n) algorithms, log-log fit"
    )


def run_special_case_experiment():
    sizes = logspace_sizes(150000, 2300000, 15)
    print(f"Speciqal case sizes: {sizes}")

    algorithms = {
        "Merge sort": merge_sort,
        "Quick sort": quick_sort,
        "Bucket sort": bucket_sort,
        "Radix sort": radix_sort
    }

    avg_times, complexity, log_sizes = run_algorithm_experiments(
        sizes, algorithms
    )

    plot_comparison(
        sizes,
        avg_times,
        "Figure: Special case vs n log n algorithms, average time"
    )

    plot_loglog_comparison(
        log_sizes,
        complexity,
        "Figure: Special case vs n log n algortihms, log-log fit"
    )


def run_nlogn_and_spcieal_case_experiment():
    sizes = logspace_sizes(150000, 2300000, 15)
    print(f"Sizes for n log n and spcieal case: {sizes}")

    algorithms = {
        "Merge sort": merge_sort,
        "Quick sort": quick_sort,
        "Bucket sort": bucket_sort,
        "Radix sort": radix_sort
    }

    avg_times, complexity, log_sizes = run_algorithm_experiments(
        sizes, algorithms
    )

    # Plot 1: Only the O(n log n) algortihms
    nlogn_avg_times = {
        label: avg_times[label] for label in ["Merge sort", "Quick sort"]
    }
    nlogn_complexity = {
        label: complexity[label] for label in ["Merge sort", "Quick sort"]
    }

    plot_comparison(
        sizes,
        nlogn_avg_times,
        "Figure: =(n log n) algorithms, average time"
    )
    plot_loglog_comparison(
        log_sizes,
        nlogn_complexity,
        "Figure: O(n log n) algorithms, log-log fit"
    )

    # Plot 2: Compare n log n to special case algortihms
    plot_comparison(
        sizes,
        avg_times,
        "Figure: Special case vs n log n, average time"
    )
    plot_loglog_comparison(
        log_sizes,
        complexity,
        "Figure: Special case vs n log n, log-log fit"
    )


def main():
    test_all_correctness()
    run_quadratic_experiment()
    run_nlogn_and_spcieal_case_experiment()


if __name__ == "__main__":
    main()

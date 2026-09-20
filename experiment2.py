import time
from quadratic_time_algorithms import (
    generate_random_list,
    selection_sort,
    bubble_sort,
    insertion_sort
)


def test_correctness(sort_func, label, original):
    lst_copy = original.copy()
    result = sort_func(lst_copy)

    print(f"=== {label} ===")
    print(f"Sorted: {result}")
    print(f"Correctly sorted: {result == sorted(original)}")
    print(f"Original unchanged: {lst_copy == original}")


def explore_sizes():
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


def main():
    print("=== Test Correctness ===")
    original = generate_random_list(10)
    print(f"Original: {original}")

    test_correctness(selection_sort, "Selection sort", original)
    test_correctness(bubble_sort, "Bubble sort", original)
    test_correctness(insertion_sort, "Insertion sort", original)

    explore_sizes()


if __name__ == "__main__":
    main()

from sorting import generate_random_list, selection_sort, bubble_sort, insertion_sort


def test_correctness(sort_func, label, original):
    lst_copy = original.copy()
    result = sort_func(lst_copy)

    print(f"=== {label} ===")
    print(f"Sorted: {result}")
    print(f"Correctly sorted: {result == sorted(original)}")
    print(f"Original unchanged: {lst_copy == original}")


def main():
    print("=== Test Correctness ===")
    original = generate_random_list(10)
    print(f"Original: {original}")

    test_correctness(selection_sort, "Selection sort", original)
    test_correctness(bubble_sort, "Bubble sort", original)
    test_correctness(insertion_sort, "Insertion sort", original)


if __name__ == "__main__":
    main()

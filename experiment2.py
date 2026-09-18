from sorting import generate_random_list, selection_sort, bubble_sort


def test_correctness(sort_func, label):
    original = generate_random_list(10)
    lst_copy = original.copy()
    result = sort_func(lst_copy)

    print(f"=== {label} ===")
    print(f"Original: {lst_copy}")
    print(f"Sorted: {result}")
    print(f"Correctly sorted: {result == sorted(original)}")
    print(f"Original unchanged: {lst_copy == original}")


def main():
    print("=== Test Correctness ===")
    test_correctness(selection_sort, "Selection sort")
    test_correctness(bubble_sort, "Bubble sort")


if __name__ == "__main__":
    main()

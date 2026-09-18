import random


def generate_random_list(n):
    return [random.randint(-1000, 1000) for _ in range(n)]


def selection_sort(lst):
    result = lst.copy()
    n = len(result)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if result[j] < result[min_index]:
                min_index = j
        result[i], result[min_index] = result[min_index], result[i]

    return result


def bubble_sort(lst):
    result = lst.copy()
    n = len(result)

    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]

    return result

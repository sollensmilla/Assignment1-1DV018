def bucket_sort(lst, num_buckets=10):
    if len(lst) == 0:
        return []

    min_val = min(lst)
    max_val = max(lst)

    if min_val == max_val:
        return lst.copy()

    range_size = (max_val - min_val) / num_buckets
    buckets = [[] for _ in range(num_buckets)]

    for x in lst:
        index = int((x - min_val) / range_size)
        if index == num_buckets:
            index -= 1
        buckets[index].append(x)

    result = []
    for bucket in buckets:
        result.extend(sorted(bucket))

    return result


def radix_sort(lst):
    if len(lst) == 0:
        return []

    negatives = [-x for x in lst if x < 0]
    non_negatives = [x for x in lst if x >= 0]

    sorted_negatives = _radix_sort_non_negative(negatives)
    sorted_non_negatives = _radix_sort_non_negative(non_negatives)

    sorted_negatives = [-x for x in reversed(sorted_negatives)]

    return sorted_negatives + sorted_non_negatives


def _radix_sort_non_negative(lst):
    if len(lst) == 0:
        return []

    result = lst.copy()
    max_val = max(result)
    exp = 1

    while max_val // exp > 0:
        result = _counting_sort_by_digit(result, exp)
        exp *= 10

    return result


def _counting_sort_by_digit(lst, exp):
    n = len(lst)
    output = [0] * n
    count = [0] * 10

    for x in lst:
        digit = (x // exp) % 10
        count[digit] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        digit = (lst[i] // exp) % 10
        output[count[digit] - 1] = lst[i]
        count[digit] -= 1

    return output

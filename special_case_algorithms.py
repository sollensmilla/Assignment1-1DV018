def bucket_sort(lst, num_buckets=10):
    if len(lst) == 0:
        return[]

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

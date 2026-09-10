"""
This file contains only the algorithms for the 3 sum problem.
"""

import random


def generate_list(n):

    return [random.randint(-10 * n, 10 * n) for _ in range(n)]


def threesum_brute(lst, sum=0):
    n = len(lst)
    result = set()

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if lst[i] + lst[j] + lst[k] == sum:
                    triplet = tuple(sorted((lst[i], lst[j], lst[k])))
                    result.add(triplet)
    return list(result)


def threesum_pointer(lst, sum=0):
    lst = sorted(lst)
    n = len(lst)
    result = set()

    for i in range(n - 2):
        left, right = i + 1, n - 1
        while left < right:
            current = lst[i] + lst[left] + lst[right]
            if current == sum:
                result.add((lst[i], lst[left], lst[right]))
                left += 1
                right -= 1
            elif current < sum:
                left += 1
            else:
                right -= 1
    return list(result)

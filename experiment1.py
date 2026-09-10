"""
This file contains the experiments for part 1. It will generate a
list of random integers and then run all the algorithms from
threesum.py.
"""

from threesum import generate_list, threesum_brute


def test_correctness():
    for run in range(3):
        lst = generate_list(15)
        result = threesum_brute(lst)
        print(f"Run {run + 1}")
        print(f"Input: {lst}")
        print(f"Result: {result}")
        print()


if __name__ == "__main__":
    test_correctness()

"""
This file contains the experiments for part 1. It will generate a
list of random integers and then run all the algorithms from
threesum.py.
"""

from threesum import generate_list, threesum_brute, threesum_pointer


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


if __name__ == "__main__":
    test_correctness()

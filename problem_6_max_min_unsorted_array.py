# referred to
# https://stackoverflow.com/questions/7604966/maximum-and-minimum-values-for-ints
# for sys.minsize,sys.maxsize
import random
import sys


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if ints == [None]:
        return None, None
    min = sys.maxsize
    max = -sys.maxsize - 1
    for i in ints:
        if i < min:
            min = i
        if i > max:
            max = i
    return min, max


cases = [
    [None],  # null case, return: (None,None), print: Pass
    [0],
    [i for i in range(0, 10)],
    [i**2 for i in range(0, 100)],
    [random.randrange(0, 100) for _ in range(10000)]
    # unusually large case, return min,max tuple, output: Pass
]


def test_function(case):
    print("Pass" if ((min(case), max(case)) == get_min_max(case)) else "Fail")


for case in cases:
    random.shuffle(case)
    test_function(case)

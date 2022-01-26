# Utilizes Dutch National Flag pseudocode from
# https://en.wikipedia.org/wiki/Dutch_national_flag_problem
from random import randrange


def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if len(input_list) < 2:
        return input_list

    mid = 1
    i = 0
    j = 0
    k = len(input_list) - 1
    while j <= k:
        if input_list[j] < mid:
            temp = input_list[i]
            input_list[i] = input_list[j]
            input_list[j] = temp
            i += 1
            j += 1
        elif input_list[j] > mid:
            temp = input_list[k]
            input_list[k] = input_list[j]
            input_list[j] = temp
            k -= 1
        else:
            j += 1
    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


cases = [
    [],  # empty case, return [], output: [], Pass
    [0],
    [1, 0],
    [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2],
    [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    [randrange(0, 3) for _ in range(10000)]
    # unusually large case, return: sorted 10000 element array with variable
    # composition of 0s,1s and 2s, output: sorted array, Pass
]

for case in cases:
    test_function(case)

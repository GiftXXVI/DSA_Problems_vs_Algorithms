def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    start = 0
    size = len(input_list)
    pivot = find_pivot(input_list, start, size-1)
    print('Pivot:', pivot, input_list[pivot], size)
    get_index(input_list, pivot, size)


def find_pivot(arr, start, end):
    mid = (start + end)//2
    if arr[mid] > arr[mid+1]:
        return mid
    if arr[start] > arr[mid]:
        end = mid
    else:
        start = mid + 1
    return find_pivot(arr, start, end)


def get_index(input_list, offset, size):
    for i, v in enumerate(input_list):
        print(i, index_in(i, offset, size), v)


def index_in(index, offset, size):
    return (index + (size - offset) - 1) % size


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


#test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
#test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
#test_function([[6, 7, 8, 1, 2, 3, 4], 8])
#test_function([[6, 7, 8, 1, 2, 3, 4], 1])
#test_function([[6, 7, 8, 1, 2, 3, 4], 10])


rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 1)
rotated_array_search([6, 7, 8, 1, 2, 3, 4], 8)
rotated_array_search([6, 7, 8, 1, 2, 3, 4, 5], 8)

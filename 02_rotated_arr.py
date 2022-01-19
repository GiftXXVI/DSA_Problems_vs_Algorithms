def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    pivot = find_pivot(input_list, 0, len(input_list)-1)
    print(pivot)
    pass


def find_pivot(arr, start, end):
    mid = (start+end)//2
    if len(arr) > 1:
        if arr[mid] > arr[mid+1]:
            return mid
        if arr[start] > arr[mid]:
            end = mid
        else:
            start = mid+1
        return find_pivot(arr[start:end], start, end)
    else:
        print(arr)
        return None


def _get_index():
    pass


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

rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 6)
rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 1)
rotated_array_search([6, 7, 8, 1, 2, 3, 4], 8)
rotated_array_search([6, 7, 8, 1, 2, 3, 4], 1)
rotated_array_search([6, 7, 8, 1, 2, 3, 4], 10)

def heapsort(input, size):
    heapify(input, size)
    end = size - 1
    while end > 0:
        temp = input[end]
        input[0] = input[end]
        input[end] = temp
        end -= 1
        sift_down(input, 0, end)


def heapify(input, size):
    start = ((size - 1) - 1) / 2
    while start>0:
        
    pass


def sift_down():
    pass


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    size = len(input_list)
    sizes = (size // 2, size - (size // 2))
    max_size = max(sizes)
    print(size, sizes, max_size)
    i = max_size
    while i > 0:
        i -= 1


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


#test_function([[1, 2, 3, 4, 5], [542, 31]])
#test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
#rearrange_digits([4, 6, 2, 5, 9, 8])
case = [4, 6, 2, 5, 9, 8]
print(heapsort(case))

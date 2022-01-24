# Utilizes HeapSort pseudocode from https://en.wikipedia.org/wiki/Heapsort

def get_iparent(index):
    return int((index - 1) / 2)


def get_ileftchild(index):
    return 2 * index + 1


def get_irightchild(index):
    return 2 * index + 2


def heapsort(input, size):
    input = heapify(input, size)
    end = size - 1
    while end > 0:
        temp = input[end]
        input[end] = input[0]
        input[0] = temp
        end -= 1
        sift_down(input, 0, end)
    return input


def heapify(input, size):
    end = size - 1
    start = get_iparent(end)
    while start >= 0:
        input = sift_down(input, start, end)
        start -= 1
    return input


def sift_down(input, start, end):
    root = start
    while get_ileftchild(root) <= end:
        child = get_ileftchild(root)
        swap = root
        if input[swap] < input[child]:
            swap = child
        if child + 1 <= end and input[swap] < input[child + 1]:
            swap = child + 1
        if swap == root:
            break
        else:
            temp_s = input[swap]
            input[swap] = input[root]
            input[root] = temp_s
            root = swap
    return input


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    size = len(input_list)

    if size < 3:
        return [None, None]

    sorted_list = heapsort(input_list, size)
    num_1 = list()
    num_2 = list()

    while len(sorted_list) > 0:
        if len(sorted_list) % 2 == 0:
            num_1.append(str(sorted_list.pop()))
        else:
            num_2.append(str(sorted_list.pop()))
    return [int(''.join(num_1)), int(''.join(num_2))]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


cases = [[[1, 1, 2], [21, 1]], [[1, 2, 3, 4, 5], [
    542, 31]], [[4, 6, 2, 5, 9, 8], [964, 852]], [[3,
                                                   4,
                                                   5,
                                                   3,
                                                   2,
                                                   8,
                                                   4,
                                                   6,
                                                   2,
                                                   1,
                                                   2,
                                                   6,
                                                   4,
                                                   7,
                                                   2,
                                                   8,
                                                   5,
                                                   6,
                                                   1,
                                                   1,
                                                   7,
                                                   8,
                                                   6,
                                                   6,
                                                   3,
                                                   1,
                                                   8,
                                                   2,
                                                   5,
                                                   2,
                                                   4,
                                                   8,
                                                   8,
                                                   3,
                                                   2,
                                                   4,
                                                   6,
                                                   1,
                                                   1,
                                                   3,
                                                   2,
                                                   3,
                                                   8,
                                                   8,
                                                   2,
                                                   3,
                                                   2,
                                                   3,
                                                   6,
                                                   1,
                                                   4,
                                                   6,
                                                   5,
                                                   1,
                                                   3,
                                                   2,
                                                   6,
                                                   6,
                                                   4,
                                                   7,
                                                   6,
                                                   1,
                                                   6,
                                                   2,
                                                   1,
                                                   8,
                                                   2,
                                                   5,
                                                   7,
                                                   6,
                                                   7,
                                                   8,
                                                   6,
                                                   3,
                                                   1,
                                                   5,
                                                   3,
                                                   7,
                                                   5,
                                                   6,
                                                   7,
                                                   6,
                                                   7,
                                                   3,
                                                   3,
                                                   4,
                                                   3,
                                                   4,
                                                   7,
                                                   7,
                                                   5,
                                                   5,
                                                   4,
                                                   4,
                                                   7,
                                                   3,
                                                   7,
                                                   6,
                                                   8,
                                                   3],
                                                  [88888877777766666666555554444433333333222222211111,
                                                   88888777777666666666555544444433333333222222111111]]]

for case in cases:
    test_function(case)


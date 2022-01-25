def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number is None:
        return (None, None)
    start = 0
    end = number
    guess = (start + end) // 2
    result = _sqrt(start, guess, end, number)

    if result is None:
        return (None, None)
    return (-result, result)


def _sqrt(start, mid, end, target):
    if target == 0:
        return 0
    elif target == 1:
        return 1
    elif target < 0:
        return None
    else:
        if mid**2 > target:
            end = mid
            mid = (start + end) // 2
            return _sqrt(start, mid, end, target)
        elif mid**2 < target:
            if (mid + 1)**2 > target:
                return mid
            else:
                start = mid
                mid = (start + end) // 2
                return _sqrt(start, mid, end, target)
        else:
            return mid


cases = [(None, None),  # null case, return: (None,None), output:Pass
         (3, 9), (0, 0), (4, 16), (1, 1), (5, 27),
         # extremely large case, return: (-3037000499,3037000499), output: Pass
         (3037000499, 9223372036854775807),
         (-3, 9), (-4, 16), (-1, 1), (-5, 27), (6, 42), (None, -4)]


def test_function(case):
    result = sqrt(case[1])
    print("Pass" if (case[0] == result[0] or case[0] == result[1]) else "Fail")


for case in cases:
    test_function(case)

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    start = 0
    end = number
    guess = (start + end)/2
    while guess**2!=number:
        if guess**2 > number:
            end = guess
            guess = (start + end)/2
        elif guess**2<number:
            if (guess + 1)**2>number:
                return guess
            else:
                start = guess
                guess = (start + end)/2
        else:
            return guess

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
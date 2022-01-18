def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    guess = number/2
    if guess**2>number:
        guess -= floor((guess + (guess/2))/2)
    else:
        if guess**2==number:
            return guess
        else:
            if guess**2<number and (guess+1)**2>number:
                return guess
            else:
                guess += floor((guess + (guess/2))/2)   
    pass

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
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
    guess = (start + end)//2
    
    
def _sqrt(start,mid,end,target):
    if mid**2 > target:
        end = mid
        mid = (start + end)//2
        return sqrt()
    elif mid**2<target:
        if (mid + 1)**2 > target:
            return mid
        else:
            start = guess
            mid = (start + end)//2
    else:
        return mid

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
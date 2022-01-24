# Problem 1: Finding the Square Root of an Integer
## Overview
This solution utilises recursion to find the largest number whose square is less than or equal to the provided input.

![Input Size vs Number of Recursive Calls](/assets/Input_Size_vs_Recursive_Calls.png "Input Size vs Recursive Calls")

## Time Complexity
The algorithm's run time depends on the magnitude of the input number. However, because the value calculated approaches the solution in increments of x^2, it eliminates all possible solution values between (x-1)^2 and x^2 between each call. Thus thus the algorithm's time complexity is O(log(n)) where n is the input number.

## Space Complexity
Since the amount of space required depends on the number of stack frames created which in turn depends on the number of loops, the space complexity of the solution is also O(log(n)).
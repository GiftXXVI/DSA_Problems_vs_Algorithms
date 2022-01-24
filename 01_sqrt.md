# Problem 1: Finding the Square Root of an Integer
## Overview
This solution utilises recursion and the binary search algorithm to find the largest number whose square is less than or equal to the provided input.

![Input Size vs Number of Recursive Calls](/assets/Input_Size_vs_Recursive_Calls.png "Input Size vs Recursive Calls")

## Time Complexity
The algorithm's run time depends on the magnitude of the input number. However, because the value calculated approaches the solution in increments of x^2, it eliminates all possible solution values between (x-1)^2 and x^2 between each call. In addition, the algorithm utilises the binary search algorithm to eliminate values of x that are greater than (or less than) the current mid. Thus this the algorithm's time complexity is O(log(n)) where n is the input number.

## Space Complexity
Since the amount of space required depends on the number of stack frames created which in turn depends on the number of loops, the space complexity of the solution is also O(log(n)).
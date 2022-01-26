# Problem 1: Finding the Square Root of an Integer

## Data Structures

This solution utilises a recursive binary search algorithm to find the largest number whose square is less than or equal to the provided input. The binary search algorithm was selected because of its desirable time complexity of O(log(n)).

![Input Size vs Number of Recursive Calls](/assets/Input_Size_vs_Recursive_Calls.png "Input Size vs Recursive Calls")

## Time Complexity

The algorithm utilises the binary search algorithm to eliminate values of x that are greater than (or less than) the current mid and compares the value of their squares to the provided number. It then eliminates half of the possible solutions in each iteration based on whether the square of the current number is greater than or equal to the input number. (It does this until it finds the largest integer square less than or equal to the input number then returns the current value of x). Thus, since it eliminates half of possible solutions in each loop, this the algorithm's time complexity is O(log(n)) where n is the input number.

## Space Complexity

Since the amount of space required depends on the number of stack frames created which in turn depends on the number of loops, the space complexity of the solution is also O(log(n)).

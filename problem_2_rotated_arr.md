# Problem 2: Search in a Rotated Sorted Array

## Data Structures

This solution uses a recursive Binary Search to find the pivot and then find the index of the search parameter. The binary search algorithm was chosen because it has the desirable time complexity of O(log(n)).

## Time Complexity

The time complexity is a sum of the complexities of the get_pivot() and get_index() functions. Both are binary searches. Thus each algorithm (and the solution as a whole) has a time complexity of O(log(n)).

## Space Complexity

The algorithm utilizes recursion. Thus the amount of space used will depend on the number of recursive calls(which determines the number of stack frames created). Thus, the space complexity of the algorithm is also O(log(n)) - as half the possible results are eliminated with each recursive call (also eliminating half of the possible function calls).

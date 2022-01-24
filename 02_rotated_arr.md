# Problem 2: Search in a Rotated Sorted Array
## Overview
This solution uses 2 binary search algorithms. The first binary search is used to find the pivot index (the point where the largest item and smallest item are located next to each other) and uses this to set an offset. The second algorithm uses the offset as an adjustment variable into a translation function.

The translation function returns a zero based index which is used to conduct a second binary search into the array as if it were a normal ordered array with the smallest item at index 0.  

## Time Complexity

The time complexity is a sum of the complexities of the get_pivot() and get_index() functions. As described above, both are binary searches. Thus each has a time complexity of O(log(n)).

## Space Complexity

The algorithm utilizes recursion. Thus the amount of space used will depend on the number of recursive calls(which determines the number of stack  frames created). Thus, the space complexity of the algorithm is also O(log(n)) - as half the possible results are eliminated with each recursive call (also eliminating half of the possible future calls).
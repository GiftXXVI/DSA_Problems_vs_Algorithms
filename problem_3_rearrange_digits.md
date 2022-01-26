# Problem 3: Rearrange Array Elements

## Data Structures

The heap data structure and the heapsort algorithm were selected because they are able to sort the array with a time complexity of O(n) which is better than the O(n log(n)) time complexity required for this problem.

## Time Complexity

The heap sort implementation is an implementation of the pseudocode found at [HeapSort - WikiPedia](https://en.wikipedia.org/wiki/Heapsort). The documentation of the pseudocode (at [HeapSort - WikiPedia](https://en.wikipedia.org/wiki/Heapsort)) states that an implementation of this algorithm using siftDown has a time complexity of O(n).

The heapsort is followed by loop that runs for as long as the sorted array has an element to pop. The time complexity of this algorithm is also O(n) as the number of iterations depends on the size of the input array.

The final step is to join the characters in the 2 arrays arrays and convert them to integers. The join has a time complexity of O(n) where n is the size of the input array. (This is O(n+m) [where n and m are the sizes of the 2 input arrays and n is greater than or equal to m], approximated to O(2n) then to O(n)).

Overall, the time complexity of this algorithm is O(n) since it consists of sequential operations that have a time comlplexity of O(n).

## Space Complexity

The algorithm reserves extra space for building the 2 numbers to be returned. These are 2 arrays of approximate size n/2 where n is the size of the input array. In addition, there are function calls that may create a copy of the array when called. The extra space requirement is proportional to the size of the input array, so the Space Complexity of the algorithm is O(n) where n is the size of the input array.

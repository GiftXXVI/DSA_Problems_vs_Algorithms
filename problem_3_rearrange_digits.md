# Problem 3: Rearrange Array Elements

## Data Structures

The heap data structure and the heapsort algorithm were selected because they are able to sort the array with a time complexity of O(n) which is better than the O(n log(n)) time complexity required for this problem.

## Time Complexity

### Heapsort

The heap sort implementation is an implementation of the pseudocode found at [HeapSort - WikiPedia](https://en.wikipedia.org/wiki/Heapsort). It consists of a call to heapify (time complexity O(nlog(n)) as explained below). This is followed by a loop from the end of the array to the beginning (through all nodes) which also encapsulates a call to heapify. As in heapify below, this loop has a complexity of O(nlog(n))

#### Heapify

Heapify consists of a loop through all elements of the array (O(n)) which contains a call to sift_down (time complexity O(log(n)) as explained below).This means that heapify has a time complexity of O(nlog(n)).

##### Sift_Down

sift_down navigates through the levels of the tree(specifically to the left child of each element from the root). It compares the left child and the current node, if the child is greater, the 2 are swapped. It then does the same for the right child. Since it navigates the levels of the tree, it has a time complexity of O(log(n)).

The heapsort is followed by loop that runs for as long as the sorted array has an element to pop. The time complexity of this algorithm is also O(n) as the number of iterations depends on the size of the input array.

The final step is to join the characters in the 2 arrays arrays and convert them to integers. The join has a time complexity of O(n) where n is the size of the input array. (This is O(n+m) [where n and m are the sizes of the 2 input arrays and n is greater than or equal to m], approximated to O(2n) then to O(n)).

Overall, the time complexity of this algorithm is O(n) since it consists of sequential operations that have a time comlplexity of O(n).

## Space Complexity

The algorithm reserves extra space for building the 2 numbers to be returned. These are 2 arrays of approximate size n/2 where n is the size of the input array. In addition, there are function calls that may create a copy of the array when called. The extra space requirement is proportional to the size of the input array, so the Space Complexity of the algorithm is O(n) where n is the size of the input array.

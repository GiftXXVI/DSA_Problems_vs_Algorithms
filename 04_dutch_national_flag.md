# Problem 4: Dutch National Flag Problem
## Overview
This solution has 3 pointers named i,j and k. 
i and j start from the beginning of the array while k starts from the end.
In each iteration of the loop, the current value of j is compared to a predefined mid value(in this case, the mid value is 1 since its magnitude lies between that of 0 and 2). If j is less than 1, it is swapped with the current value at index i and i and j are incremented. If j is greater than 1, it is swapped with the current value of k and j is incremented k is decremented. The loop stops when j and k point to the same location.

## Time Complexity
The algorithm performs n - J comparisons (where J is the final value of the pointer j). Thus the time complexity is O(n).

## Space Complexity
All operations happen in place, therefore the space complexity of this algorithm is O(1). 
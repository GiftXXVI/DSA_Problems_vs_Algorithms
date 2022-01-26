# Problem 5: Autocomplete with Tries

## Data Structures

This solution utilizes a Trie data structure as prescribed.

## Time Complexity

The time complexities for the individual Trie operations is defined below:

### Constructors

All constructors for the Trie and TrieNode consists of O(1) operations. (the number of steps in the operations does not vary with input size).

### insert

The insert method calls the TrieNodes find method. If it does not find the input text, it iterates through each character of the input text and inserts it into the Trie. 

All other operations and function calls such as: 
- the TrieNode map_chr method.
- the TrieNode insert method.
- and other steps
are O(1) operations because they all locate a dictionary element using its key.
 
Thus the time complexity of this function is O(n). 

### find/contains

The find method iterates through each character in the input text up to the last character and returns the last node. The time complexity of this operation is O(n) because navigation through the Trie is done by searching the children Dictionary for the current character (The time complexity of each search is O(1)). So overall, the run time is proportional to the size of the input string, thus the time complexity of the method is O(n).

### suffixes

The suffixes method first calls find to locate the last node of the input text in the Trie. This operation has a time complexity of O(n).

Then, a recursive function iterates through all children of the current node and finds all sub-Tries that end in a node that has "is_terminal" set to True. It visits all nodes in the sub-Trie of the current node to find all words in the sub-Trie. This means that the time complexity of the algorithm is O(n) where n is the size of the sub-Trie.

Overall, the time complexity of the algorithm is O(n), where n is the number of nodes in the sub-Trie.

## Space Complexity
### insert
The space complexity of insert is O(n) where n is the size of the input string.

### find/contains
These methods have a space complexity of O(1) since they do not require any extra space to perform their search.

### suffixes
The suffixes method is recursive, with the number of function calls depending on the number of nodes of the current sub-Trie. Since each recursive call generates a new stack frame, the space complexity of the algorithm is O(n) where n is the number of sub-Tries of the node.

# Problem 5: Autocomplete with Tries

## Data Structures

This solution utilizes a Trie data structure as prescribed.

## Time Complexity

The time complexities for the individual Trie operations is defined below:

### Constructors

All constructors for the Trie and TrieNode consists of O(1) operations. (the number of steps in the operations does not vary with input size).

### Trie methods (including TrieNode method calls)

#### insert

The insert method calls the TrieNodes find method. If it does not find the input text, it iterates through each character of the input text and inserts it into the Trie.

All other operations and function calls such as:

- the TrieNode map_chr method.
- the TrieNode insert method.
- and other steps
  are O(1) operations because they all locate a dictionary element/list element using its key/index.

Thus the time complexity of this function is O(n).

#### find/contains

The find method iterates through each character in the input text up to the last character and returns the last node.

It contains a call to the map_chr method of the TrieNode which has a time complexity of O(1) because it uses a key to access a dictionary(hash table/associative array) element.

The time complexity of all other operation in and around the loop is O(1).

The time complexity of the find/contains methods is O(n) because of the loop through the characters of the input text.

### TrieNode methods

### suffixes

The suffixes method first calls find to locate the last node of the input text in the Trie. This operation has a time complexity of O(n).

#### \_suffixes

suffixes calls a recursive function ,\_suffixes, which iterates through all children of the current node and finds all sub-Tries that end in a node that has "is_terminal" set to True. It visits all nodes in the sub-Trie of the current node to find all words in the sub-Trie.

This loop contains a final step to add the words to the return array. This has a time complexity of O(m) where m is the size of the array of words being added to the result.

Overall, the time complexity of the suffixes method is O(n\*m) or O(n^2).

## Space Complexity

### insert

The space complexity of insert is O(n) where n is the size of the input string.

### find/contains

These methods have a space complexity of O(1) since they do not require any extra space to perform their search.

### suffixes

The suffixes method is recursive, with the number of function calls depending on the number of nodes of the current sub-Trie. Since each recursive call generates a new stack frame, the space complexity of the algorithm is O(n) where n is the number of sub-Tries of the node.

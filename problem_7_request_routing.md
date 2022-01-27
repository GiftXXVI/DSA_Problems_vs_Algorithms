# Problem 7: Request Routing in a Web Server with a Trie

## Data Structures

This algorithm uses a Trie data structure as prescribed.

## Time Complexity

### Constructors

All constructors (for the Route, RouteTrie and RouteTrieNode) contain only simple operations that have a time complexity of O(1).

### add_handler

add_handler calls the split_path function. The time complexity of the split_path function is O(n) where n is the number of segments of the path.

Since the function executes two subsequent functions,split_path and RouteTrie insert(explanation in the next paragraph), both of which have a time complexity of O(n), it has a time complexity of O(n).

#### insert (RouteTrie)

The RouteTrie insert method loops through the segments and calls the RouteTrieNode insert method for each segment. The RouteTrieNode insert method has a time complexity of O(1) because it inserts a new element into a dictionary using a key.Therefore, the RouteTrie insert methood has a time complexity of O(n) where n is the number of path segments.

### lookup

The lookup function also has a time complexity of O(n). This is because it calls the split_path function (which has a time complexity of O(n)) followed by a call to the find function of the Trie. (explanation in the paragraph below)

#### find (RouteTrie)

The find function also has a time complexity of O(n) because it loops through the path, finding the node matching the value of the current path segment and searching its child nodes for the a node matching the next segment until it reaches the end of the path.

### split_path

The split path function uses the string split method, which has a time complexity of O(n).

## Space Complexity

### add_handler

add_handler calls split_path and RouteTrie insert.

split_path creates an array of size corresponding to the number of path segments (this means it has O(n) space complexity).

This is followed by RouteTrie insert creates a RouteTrieNode instance for each path segment (this also means it has O(n) space complexity).

Thus overall, the space complexity is O(n).

### lookup

This method (including the call to the RouteTrie find method) has a space complexity of O(1) since it does not require any extra space to perform a search.

### split_path

split_path does not create an additional space during the operation.

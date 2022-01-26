# Problem 7: Request Routing in a Web Server with a Trie

## Data Structures

This algorithm uses a Trie data structure as prescribed.

## Time Complexity

### add_handler

add_handler calls the split_path function. The time complexity of the split_path function is O(n) where n is the number of segments of the path.

It then calls insert on the Trie object, which also has a time complexity of O(n) where n is the number of path segments. This is because it inserts the segments into the Trie one at a time (each subsequent segment is a child of the previous one).

Since the function executes two subsequent functions, both of which have a time complexity of O(n), it has a time complexity of O(n).

### lookup

The lookup function also has a time complexity of O(n). This is because it calls the split_path function (which has a time complexity of O(n)) followed by a call to the find function of the Trie. 

The find function also has a time complexity of O(n) because it searches the children of a node (matching the current segment) for the next node (matching the next segment).

### split_path

The split path function uses the string split method, which has a time complexity of O(n).

## Space Complexity

### add_handler

The space complexity of insert is O(n) where n is the size of the input string since it creates a node for each segment of the path.

### lookup

This method has a space complexity of O(1) since it does not require any extra space to perform a search.

### split_path

split_path does not create an additional space during the operation.
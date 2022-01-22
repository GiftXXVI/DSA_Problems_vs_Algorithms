# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root
        # path or home page node
        self.root = RouteTrieNode()

    def insert(self, path):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of
        # this path
        node = self.root
        sections = path.split('/')
        for index, section in enumerate(sections):
            if section not in node.children:
                node.children[section] = section
            node = node.children[section]
            if index == len(sections):
                node.is_terminal = True

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match

        node = self.root
        sections = path.split('/')
        for index, section in enumerate(sections):
            if section not in node.children:
                return None
            node = node.children[section]
        if node.is_terminal:
            return node
        return None

# A RouteTrieNode will be similar to our autocomplete TrieNode... with
# one additional element, a handler.


class RouteTrieNode:
    def __init__(self, value='/', terminal=False):
        # Initialize the node with children as before, plus a handler
        self.is_terminal = terminal
        self.value = value
        self.children = dict()

    def insert(self, value, terminal):
        # Insert the node as before
        self.children[value] = RouteTrieNode(
            value=value, terminal=terminal)


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as
        # well!
        pass

    def add_handler(self):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        pass

    def lookup(self):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        pass

    def split_path(self):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here

        # Here are some test cases and expected outputs you can use to test
        # your implementation

        # create the router and add a route
        # remove the 'not found handler' if you did not implement this
        pass


router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home"))
print(router.lookup("/home/about"))  # should print 'about handler'
# should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/"))
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about/me"))

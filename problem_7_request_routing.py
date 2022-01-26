class Handler():
    def __init__(self, response, code):
        self.response = response
        self.code = code

    def __repr__(self):
        return f'{str(self.code)}: {self.response}'


# A RouteTrie will store our routes and their associated handlers


class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root
        # path or home page node
        self.root = RouteTrieNode()

    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of
        # this path
        node = self.root
        if self.find(path) is None:
            for index, section in enumerate(path):
                if section not in node.children:
                    node.insert(section)
                node = node.children[section]
            node.handler = Handler(handler, 200)
            node.is_terminal = True

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match

        node = self.root
        if path[0] == node.value:
            return node
        for index, section in enumerate(path):
            if section not in node.children:
                return None
            node = node.children[section]
        if node.is_terminal:
            return node
        return None

# A RouteTrieNode will be similar to our autocomplete TrieNode... with
# one additional element, a handler.


class RouteTrieNode:
    def __init__(self, value='/', terminal=False, handler=None):
        # Initialize the node with children as before, plus a handler
        self.is_terminal = terminal
        self.value = value
        self.children = dict()
        self.handler = handler

    def insert(self, value):
        # Insert the node as before
        self.children[value] = RouteTrieNode(value=value)

    def __repr__(self):
        return f'<RouteTrieNode value:{self.value},is_terminal:{self.is_terminal},handler:{self.handler}>'


# The Router class will wrap the Trie and handle


class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as
        # well!
        self.trie = RouteTrie()
        self.error_handler = Handler(not_found_handler, 404)
        if root_handler is not None:
            self.add_handler('/', root_handler)

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        if self.lookup(path) == self.error_handler:
            self.trie.insert(self.split_path(path), handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if path is None or len(path) == 0:
            return self.error_handler
        node = self.trie.find(self.split_path(path))
        if node is None:
            return self.error_handler
        return node.handler

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        if path[len(path) - 1] == '/':
            path = path[:len(path) - 1]
        return path.split('/')

        # Here are some test cases and expected outputs you can use to test
        # your implementation

        # create the router and add a route
        # remove the 'not found handler' if you did not implement this


router = Router("root handler", "not found handler")
cases = [
    ('/home/about', 'about handler'),
    ('/home/features', 'features handler'),
    ('/home/news', 'news handler'),
    ('/home/news/science', 'science handler'),
    ('/home/news/science/12201-tonga-volcano-erupts', 'tonga volcano handler'),
    ('/home/news/science/12301-james-webb-launches', 'james webb launch handler'),
    ('/home/news/sports', 'sport'),
    ('/home/news/technology', 'technology handler'),
    ('/home/news/technology/12341-ai-fighter-pilots', 'ai fighter pilots handler'),
    ('/home/kb/engineers', 'engineers kb handler'),
    ('/home/kb/users', 'users kb handler'),
    ('/home/blog/77091-monday-motivation-100', 'monday motivation 100 handler'),
    ('/home/blog/93803-boosting-performance-in-short-time-101',
     'performance 101 handler'),
    ('/home/locations/malawi/lilongwe', 'lilongwe handler'),
    ('/home/locations/malawi/blantyre', 'blantyre handler'),
    ('/home/reviews', 'reviews handler'),
    ('/home/contacts', 'contacts handler'),
    ('/home/about', 'about handler')]
for case in cases:
    router.add_handler(case[0], case[1])  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
# should print 'not found handler' or None if you did not implement one

print(router.lookup("/home"))
print(router.lookup("/home/about"))  # should print 'about handler'
# should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/"))
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about/me"))

print(router.lookup(""))  # empty case, return and print 404: not found handler
print(router.lookup(None))  # null case, return and print 404: not found handler

# %%
# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.


class RouteTrieNode:
    def __init__(self, value: str, handler="not found handler"):
        # Initialize the node with children as before, plus a handler
        self.value = value
        self.children = {}
        self.handler = handler

    def insert(self, value: str):
        # Insert the node as before
        self.children[value] = RouteTrieNode(value)

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode("/", handler)
    
    def insert(self, route: list, handler: str):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        trie_node = self.root

        for value in route:
            if value in trie_node.children:
                trie_node = trie_node.children[value]
            else:
                trie_node.insert(value)
                trie_node = trie_node.children[value]

        trie_node.handler = handler

    def find(self, route: list):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        trie_node = self.root

        for value in route:
            if value in trie_node.children:
                trie_node = trie_node.children[value]
            else:
                return None
        return trie_node.handler


# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_trie = RouteTrie(root_handler)

    def add_handler(self, route, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        route_cleaned = self.split_path(route)
        self.route_trie.insert(route_cleaned, handler)

    def lookup(self, route):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if not isinstance(route, str):
            raise ValueError("Please provide path as str.")
        route_cleaned = self.split_path(route)
        handler = self.route_trie.find(route_cleaned)
        return handler if handler else "not found handler"

    def split_path(self, route):
        # you need to split the path into parts for 
        # both the add_handler and lookup functions,
        # so it should be placed in a function here
        return list(filter(lambda x: x != "", route.split("/")))

# %%
# Here are some test cases and expected outputs you can use to test your implementation
# create the router and add a route
router = Router("root handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# %%
# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one

router.lookup("") # Edge case: empty string
router.lookup(None) # Edge case: None input

# %%

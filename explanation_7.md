## Problem 7: Request Routing in a Web Server with a Trie
For this exercise we are going to implement an HTTPRouter like you would find in a typical web server using the Trie data structure.

### Efficiency
I re-used most parts of the auto-completion trie data structure (Problem 5). This code stores an additional attribute for each node to keep track of the handler for each route.
Furthermore, the Router class is defined which wraps the RouteTrie functionality and acts as an "interface" between the user and the underlying Trie data structure.

Inserting and finding a route handler works in O(n) time. The space complexity of the Trie is the sum of all the Nodes in the Trie. The space complexity for the insertion of a new route handler is O(n).
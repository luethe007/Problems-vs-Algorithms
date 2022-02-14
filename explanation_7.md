## Problem 7: Request Routing in a Web Server with a Trie
For this exercise we are going to implement an HTTPRouter like you would find in a typical web server using the Trie data structure.

### Efficiency
This code stores an additional attribute for each node to keep track of the handler for each route.
Furthermore, the Router class is defined which wraps the RouteTrie functionality and acts as an "interface" between the user and the underlying Trie data structure.

Inserting and finding a route handler works in O(n) time. The space complexity of the Trie is the sum of all the Nodes in the Trie. The space complexity for the insertion of a new route handler is O(n).

#### RouteTrieNode Complexity Analysis  
The creation of a RouteTrieNode works in O(1) time and requires constant space O(1). Inserting a child RouteTrieNode also works in constant time and requires constant space.

#### RouteTrie Complexity Analysis  
The creation of a RouteTrieTrie works in O(1) time and requires constant space O(1).
Both the "insert" and "find" functions iterate over the route components, resulting in linear time complexity O(n).
The space complexity of the Trie is the sum of all the Nodes in the Trie. The space complexity for the insertion of one path is O(n).

#### Router Complexity Analysis  
The creation of a Router requires O(1) time complexity and O(1) space complexity.
The time and space complexity of the "add_handler" function is linear O(n).
The "lookup" also works iteratively in O(n) time and requires constant space O(1).

## Problem 5: Autocomplete with Tries
Implement an autocomplete function using Tries. Create a TrieNode object that will return all complete word suffixes that exist below it in the Trie.  

### Efficiency
The Trie is a tree-structure which is used to provide auto-completion features. I implemented a TrieNode and a Trie class. The TrieNode instances represent character values and point down towards the children. The Trie class is used to initialize the tree structure. The empty Trie only contains a root node representing an empty string. This is the starting point for any insertion or finding procedure. The search for suffixes for the auto-completion uses recursion to step downwards through the tree.

#### TrieNode Complexity Analysis  
The creation of a TrieNode works in O(1) time and requires constant space O(1).
The insertion of a TrieNode as a child of a given Node also works in O(1) time.
The function "suffixes()" recursively walks through all the downstream nodes in the tree. This works in linear time O(n) and requires O(n) space.

#### Trie Complexity Analysis  
The creation of a Trie works in O(1) time and requires constant space O(1).
Both the "insert" and "find" functions iterate over the words, resulting in linear time complexity O(n). 
The space complexity of the Trie is the sum of all the Nodes in the Trie. The space complexity for the insertion of one word is O(n).
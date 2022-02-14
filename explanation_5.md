## Problem 5: Autocomplete with Tries
Implement an autocomplete function using Tries. Create a TrieNode object that will return all complete word suffixes that exist below it in the Trie.  

### Efficiency
The Trie is a tree-structure which is used to provide auto-completion features. I implemented a TrieNode and a Trie class. The TrieNode instances represent character values and point down towards the children. The Trie class is used to initialize the tree structure. The empty Trie only contains a root node representing an empty string. This is the starting point for any insertion or finding procedure. The search for suffixes for the auto-completion uses recursion to step downwards through the tree.

Inserting and finding a prefix works in O(n) time. The space complexity of the Trie is the sum of all the Nodes in the Trie. The space complexity for the insertion of one word is O(n).
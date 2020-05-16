# Problem 5: Autocomplete with Tries

# Design Choice:
I've used **Trie** which is a tree-like data structure to store dynamic strings. Tries are space efficient and thus, i've used this to store strings. For suffixes method in TrieNode i'used **Recursion** to traverse the Trie to find the suffixes of the given node and a **list** to store the suffixes of the given node.

# Time complexity:
**O(m)** for inserting and finding the node (m - length of the word)
**O(n)** for finding suffixes (n - number of keys from the given node)

# Space complexity:
**O(k * m)** where k is number of keys and m is length of the word.
# Problem 7: HTTPRouter using a Trie

# Design Choice:
I've used **Trie** data structure to solve this problem because it is an excellent and very efficient data structure for this purpose.
In this problem, we have a Router class which has 3 different methods.The first method is add_handler which is used to add handler at a specified path in the RouteTrie, The lookup method is used to find the handler of a given path if exist else it will throw "not found handler".
split_path method is used to split the given path by a '/' separator.

# Time complexity:
**O(n)** for adding handler and finding the handler (n - parts of the path)

# Space complexity:
**O(k * m)** where k is number of keys and m is parts of the path.
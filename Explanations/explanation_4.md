# Problem 4: Dutch National Flag Problem

# Design Choice:
No special algorithms are used to sort the list. A simple logic is used to sort the elements in an ascending order. The logic is to put 0 and 2 in their correct positions, which will make sure all the 1s are automatically placed in their right positions and the sorting is done in single traversal which makes this problem more efficient than using other sorting algorithms for this problem.

# Time complexity:
**O(n)** for traversing the unsorted list to sort. (n - size of the list)

# Space complexity:
**O(1)** - Actions are performed in the given list and no new data structure is used.
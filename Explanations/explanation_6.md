# Problem 6: Max and Min in a Unsorted Array

# Design Choice:
No special algorithms are used to find min and max of the given list. Initially we have to assign first element as a min and max and have to compare the assigned min and max with the elements in the given list, If the number is minimum than the min value than, we just have to swap the element with the min and for max, If the number is maximum than the max value than, swap the element with the max. Finding of min and max is done in single traversal.

# Time complexity:
**O(n)** for traversing the unsorted list. (n - size of the list)

# Space complexity:
**O(1)** - Actions are performed in the given list and no new data structure is used.
# Problem 2: Search in a Rotated Sorted Array

# Design Choice:
I've used **Binary Search Algorithm** to Search in a rotated sorted array because, it has less time complexity and space complexity compared to other algorithms.
First we have to divide the rotated sorted array into two halfs and check whether first half is sorted, if first half is sorted than we have to find the element in first half else, if first half is not sorted than we have to find the element in the second half and check whether the element is in the second half, If element is not present in the second half then search in the first half.

# Time complexity:
**O(logn)** where n is the size of the rotated sorted array

# Space complexity:
**O(1)** - Actions performed on the given list only, no new data structure is used
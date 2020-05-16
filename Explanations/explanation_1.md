# Problem 1: Finding the Square Root of an Integer

# Design Choice:
I've used **Binary Search Algorithm** to find the square root of the given number because, it has less time complexity and space complexity compared to other algorithms.
Binary search is usually helps to find a number by dividing the parts into two with divider as mid point and repeats the process until midpoint matches the given number.
In this case, we will just compare the square of the mid value with the given square in each step, if square of the mid value matches the given square then, we return the mid value (square root) else if the given square is not a perfect square we will return the mid value of a perfect square which is nearby to the given square.

# Time complexity:
**O(logn)** where n is the given square root

# Space complexity:
**O(1)** only variables are used to store data which are instant
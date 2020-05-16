# Problem 3: Rearrange Array Elements

# Design Choice:
I've used **Merge Sort** to sort the array in a descending order, it has less worst case time complexity to sort as compared to other algorithms.
In the sorted list, the evenly distributed elements in the list are the first max sum of the given list and the rest of the digits forms second max sum of the given list for e.g [5, 4, 3, 2, 1] then 5,3,1 are evenly distributed which forms the first max sum and the remaining digits 4,2 forms the second max sum.

# Time complexity:
**O(nlogn)** for sorting the array and **O(n)** is for traversing the sorted list to find first max sum and second max sum.
*Total complexity* = O(nlogn) + O(n) = **O(nlogn)**

# Space complexity:
**O(n)** to store the sorted elements.
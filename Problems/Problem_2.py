#!/usr/bin/env python
# coding: utf-8

# # Problem 2 - Search in a Rotated Sorted Array

# In[102]:


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    
    if not input_list or not number:
        return -1
        
    return binary_search(input_list, number, 0, len(input_list)-1)
    
def binary_search(arr, target, start_index, end_index):
    
    # Base Case
    if start_index > end_index:
        return -1
    
    mid_index = (start_index + end_index) // 2
    
    if arr[mid_index] == target:    # If the target found returns the index
        return mid_index
    
    # Checks whether the first half of arr is sorted
    if arr[start_index] <= arr[mid_index]:    
        
        # If the target is in between the first half, the target will be searched init
        if arr[start_index] <= target <= arr[mid_index]:    
            return binary_search(arr, target, start_index, mid_index)
        else:    # Else it will search the target in the other half
            return binary_search(arr, target, mid_index + 1, end_index)
    
    # If the first half is not sorted it will search target in the second half
    elif arr[mid_index] < target < arr[end_index]:  
        return binary_search(arr, target, mid_index + 1, end_index)
        
    # If target is not in the second half it will search the target in the first half
    return binary_search(arr, target, start_index, mid_index - 1)
   


# # Test Cases

# In[103]:


def linear_search(input_list, number):
    if not input_list:
        return -1
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[5,1,2,3,4], 1])


# # Edge Test Cases

# In[104]:


# Empty Input
test_function([[], 6])


# In[105]:


# Large Input
first_half = [x for x in range(2000, 5000)]
second_half = [y for y in range(0, 2000)]
rotated_arr = first_half + second_half

# Target in range
test_function([rotated_arr, 2555])

# Target out of range
test_function([rotated_arr, 50000])


# In[106]:


# Null Input
test_function([[], None])
test_function([None, 3])
test_function([None, None])


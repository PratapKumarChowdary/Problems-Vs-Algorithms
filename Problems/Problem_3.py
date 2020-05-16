#!/usr/bin/env python
# coding: utf-8

# # Problem 3 - Rearrange Array Elements

# In[38]:


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    
    if not input_list:
        return None
    
    first_max_sum = ""
    second_max_sum = ""
    
    # Sort the elements in descending order
    desc_sort = merge_sort(input_list)
    
    # The evenly distributed elements in the list are the first max sum of the given list
    # and the rest of the digits forms second max sum of the given list
    # for e.g [5, 4, 3, 2, 1] then 5,3,1 are evenly distributed which forms the first max sum 
    # and the remaining digits 4,2 forms the second max sum
    for index, el in enumerate(desc_sort):
        if index % 2 == 0:
            first_max_sum += str(el)
        else:
            second_max_sum += str(el)
        
    return int(first_max_sum), int(second_max_sum)
    

def merge_sort(input_list):
        
    if len(input_list) <= 1:
        return input_list
    
    mid_index = len(input_list) // 2
    
    left_half = input_list[:mid_index]
    right_half = input_list[mid_index:]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    return merge(left_half, right_half)


def merge(left_half, right_half):
    
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left_half) and right_index < len(right_half):
        
        if left_half[left_index] < right_half[right_index]:
            merged.append(right_half[right_index])
            right_index += 1
        else:
            merged.append(left_half[left_index])
            left_index += 1
        
    merged += left_half[left_index:]
    merged += right_half[right_index:]
    
    return merged


# # Test Cases

# In[39]:


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])


# # Edge Test Cases

# In[40]:


# Empty Input
print(rearrange_digits([]))


# In[41]:


# Null Input
print(rearrange_digits(None))


# In[36]:


# Large Input
import random

l = [i for i in range(0, 1000)]    # a list containing 0 - 999
random.shuffle(l)

print("First max sum :-")
print(rearrange_digits(l)[0])
print()
print("Second max sum :-")
print(rearrange_digits(l)[1])


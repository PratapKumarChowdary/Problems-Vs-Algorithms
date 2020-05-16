#!/usr/bin/env python
# coding: utf-8

# # Problem 4 - Dutch National Flag Problem

# In[3]:


def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.
    
    The idea is to put 0 and 2 in their correct positions, which will make sure
    all the 1s are automatically placed in their right positions

    Args:
       input_list(list): List to be sorted
    """
    
    # If list is empty
    if not input_list:
        return input_list
    
    # initialize pointers for next positions of 0 and 2
    next_pos_0 = 0
    next_pos_2 = len(input_list) - 1

    front_index = 0

    while front_index <= next_pos_2:
        if input_list[front_index] == 0: # If the element is 0, place element at next position
            input_list[front_index] = input_list[next_pos_0]
            input_list[next_pos_0] = 0
            next_pos_0 += 1
            front_index += 1
        elif input_list[front_index] == 2: # If the element is 2, place element at next position of 2
            input_list[front_index] = input_list[next_pos_2] 
            input_list[next_pos_2] = 2
            next_pos_2 -= 1
        else:
            front_index += 1
    return input_list


# # Test Cases

# In[4]:


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])


# # Edge Test Cases

# In[5]:


# Empty Input
test_function([])


# In[6]:


# Null Input
print(sort_012(None))


# In[8]:


# Large Input
import random

zeros = [0 for _ in range(400)]
ones = [1 for _ in range(400)]
twos = [2 for _ in range(400)]

test_case = zeros + ones + twos
random.shuffle(test_case)

test_function(test_case)


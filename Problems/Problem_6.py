#!/usr/bin/env python
# coding: utf-8

# # Problem 6 - Max and Min in a Unsorted Array

# In[10]:


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    
    # If list has no elements return None
    if not ints:
        return None

    # If the size of the list is 1 than return the present element as min and max
    if len(ints) == 1:
        return (ints[0], ints[0])
    
    # Initially assign first element as a min and max element
    minimum = ints[0]    
    maximum = ints[0]
    
    for num in ints:
        # Compare the assigned min and max with the elements in the given list
        if minimum > num:    # If the number is minimum than the min value than, swap the element with the min
            minimum = num
        if maximum < num:    # If the number is maximum than the max value than, swap the element with the min
            maximum = num
            
    return (minimum, maximum)


# # Test Cases

# In[11]:


## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print ("Pass" if ((43, 1122) == get_min_max([233, 535, 43, 1122, 55])) else "Fail")
print ("Pass" if ((1, 1) == get_min_max([1, 1])) else "Fail")


# # Edge Test Cases

# In[12]:


# List with only element
print ("Pass" if ((22,22) == get_min_max([22])) else "Fail")


# In[13]:


# Empty Input
print ("Pass" if (None == get_min_max([])) else "Fail")


# In[14]:


# Null Input
print ("Pass" if (None == get_min_max(None)) else "Fail")


# In[15]:


# Large Input
input_list = [x for x in range(55, 5556)]

print ("Pass" if ((55, 5555) == get_min_max(input_list)) else "Fail")


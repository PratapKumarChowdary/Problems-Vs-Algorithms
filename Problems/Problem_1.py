#!/usr/bin/env python
# coding: utf-8

# # Problem 1 - Finding the Square Root of an Integer

# In[16]:


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number == 0:
        return 0
    
    if not number:
        return None
    
    # Binary Search to find the floor square root of a number
    start = 0    # Starting range of BS
    end = number    # Ending range of BS

    while start <= end:    

        center = (start + end) // 2    # Obtain center by Integer division

        mid_square = center * center    # Find square of the center

        if mid_square == number:    # If number is a perfect square
            return center

        # If number is not a perfect square then
        # we will just find the square that is just less
        # than the number and return the root of that
        elif mid_square < number:    # If square < number, then we will search in the right range (center+1 to end)
            start = center + 1
            floor_sqrt = center    # Root of the perfect square that is just less than the target number

        else:    # If square > number, then we will search in the left range (start to center-1)
            end = center - 1

    return floor_sqrt  


# # Test Cases

# In[17]:


print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")


# # Edge Test Cases

# In[22]:


# "None" as Input
print ("Pass" if  (None == sqrt(None)) else "Fail")

# Edge case
print ("Pass" if  (0 == sqrt(0)) else "Fail")

# Large Input
print ("Pass" if  (1000 == sqrt(1000000)) else "Fail")


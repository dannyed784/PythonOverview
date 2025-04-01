# 02 - flow-control - list slicing

import os
os.system("clear")

list1 = [1,2,3,4,5]
print(list1[1:4]) # it doesn't include the last index
print(list1[:3]) # til index 3 it doesn't include last index
print(list1[3:]) # index 3 to first index it includes index 3(number 4)

# to copy a list
print(list1[:]) 

# step 
# list[start:stop:step]
list2 = [1,2,3,4,5,6,7,8,9,10]
print(list2[::2])
print(list2[::3])
print(list2[::-1]) # Return the indices inverted [10,9,8,7,6,....]

# Modified a list
list2[0] = 23
print(list2)

# Add element to a list

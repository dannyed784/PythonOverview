# 02 list part-2 - flow control 
import os
os.system("clear")

list2 = [1,2,3,4,5,6,7,8,9,10]

# Modified a list
list2[0] = 23
print(list2)

# Add elements to a list
list2 = [1,2,3]

print(list2)

#larger way to add a list
list2 = list2 + [4,5,6] # it's going to be add to the end of the list
print(list2)

#shorter way to add a list
list2 += [7,6,5]

#Modify a list
list2[0]= 20
print(list2)

#to get the length of a list
print('The length of the list is: ', len(list2))

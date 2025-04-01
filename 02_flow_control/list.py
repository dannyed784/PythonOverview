# 02 - flow control - list
#create a list
import os
os.system("clear")

list1 = [1,2,3,4,5]
list2 = ["apple","pear","plantain"]
list3 = [1,"hello",3.14,True] # mixed list
empty_list = []
list_list = [[1,2],[2,3]]
matrix = [[1,2],[2,3],[4,5]]

print(list1)
print(list2)
print(list3)
print(empty_list)
print(list_list)
print(matrix)

print("\n Access to list elements: ")
print(list1[2])
print(list2[1])
print("\n Access in a negative way: ")
print(list2[-1])
print(list2[-2])
print("\n Access into the matrix: ")
print(matrix[1][1]) # 3
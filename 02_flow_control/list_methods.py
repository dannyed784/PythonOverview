#02 list methods - flow control
import os
os.system("clear")

list1 = [1,2,3,4,5]
list2 = ['a','b','c','d']
print(list1)
# append() to add an elemtent at the end of the list
list1.append(6)
print(list1)

# insert(index,element) ot insert an element in between 
print(list2)
list2.insert(1,'@')
print(list2)

# extend() add more than 1 element to the end of the list
list1.extend([3,6]) #is very similar to concat list(+ [3,6])
print(list1)

# remove() to remove an element from a list
list2.remove('@') #only will remove the first @
print(list2)

# pop() to remove the last element of the list and it will return the element
last_element = list2.pop()
print(list2)
print(last_element)

# pop(index) to remove using the index of the element
list1.pop(1)
print(list1)

# del = to delete an element - no recommended 
del list1[-1]#it support negative index
print(list1)

# clear() to delete all the elements from a list
list1.clear()
print(list1)

# delete elements using a range
list3 = ['🐵','🦊','🦝','🐰','🐹','🐯','🦁']
del list3[1:3]
print(list3)

# organize lists
print('Organize lists: ')
numbers = [3,10,2,8,99,101]
# sort() to organize a list but it modify the origianl list
numbers.sort()
print(numbers)
# sorted() to organize a list but it create a new list and you can save the list
sorted_list = sorted(numbers)
print(sorted_list)

fruits = ['apple','peach','lime','peach','lime']
sorted_fruits = sorted(fruits)
print(sorted_fruits)

#the uppercase is going to be first in the list 
fruits2 = ['Apple','Peach','lime','peach','lime']
sorted_fruits2 = sorted(fruits2)
print(fruits2)

#sort(key=str.lower) to compare just with lowercase
fruits2.sort(key=str.lower)
print(fruits2)

#More useful methods for lists
animals = ['🐵','🦊','🦝','🐰','🐹','🐯','🦁','🐯','🦝','🐵','🦝']
# count() how many times a list have an element
print(animals.count('🦝')) # how many times the list have this element

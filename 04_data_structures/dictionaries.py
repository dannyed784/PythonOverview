# dictionary = a collection of (key:value) pairs
#              ordered and changeable. No duplicates
import os
os.system("clear")

capitals ={"USA":"Washintong D.C",
           "India":"New Delhi",
           "China":"Beijing",
           "Russia":"Moscow"}

# to get all the dictoinary properties use dir()
# print(dir(capitals))
# to get help of each dictionary properties help()
# print(help(capitals))

# get() = you will get the value 
print(capitals.get("USA"))

# to add a key update()
capitals.update({"Germany":"Berlin"})
capitals.update({"USA":"Detroit"})

print(capitals)

#to remove a key value pop()
capitals.pop("China")

print(capitals)

#to remove the last key value inside the dictionary popitem()
capitals.popitem()

print(capitals)

# to clear the dictionary use clear()
# capitals.clear()

#to get all the keys of a dictionary keys()
keys = capitals.keys()
print(keys)

for key in capitals.keys():
    print(key)

#to get all the values values()
values = capitals.values()  
print(values)  

for value in capitals.values():
    print(value)

#to get all the items items()   
items = capitals.items() 
print(items)

for key, value in capitals.items():
    print(f"{key}:{value}")

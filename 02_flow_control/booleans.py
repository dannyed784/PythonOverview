# 02 - flow-control - Booleans
import os
os.system("clear")

#Comparison operators
print("5 > 3: ", 5>3)
print("5 < 3: ", 5<3)
print("5 == 5: ", 5 == 5)
print("5 != 3: ", 5 != 3)
print("5 >= 5: ", 5 >= 5)
print("5 <= 3: ", 5 <= 3)

#Strings comparison
# Because of the ASCII code and it is case sensitive
print("manzana < pera ", "manzana" < "pera" ) # True

#always number 0 is consider as a False
number = 5
number2 = 0
if number:
    print("The number is not zero")
else:
    print("The number is zero")    


if not number2:
    print("The number is zero")   
else:
    print("The number is not zero")    

#the same with the string, a empty string is always zero
name = "Daniel"
name2 =""
if name:
    print("The name is not empty")
else:
    print("The name is empty")    
if not name2:
    print("The name is empty")    

#Comparison and assignment
number3 = 3
is_it_number_3 = number3 == 3 #True

if is_it_number_3:
    print("is it number 3")

#Ternary operators
age = 18
message = "Adult" if age>=18 else "Minor"   
print(message)
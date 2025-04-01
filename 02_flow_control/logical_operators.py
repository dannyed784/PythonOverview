# 02 - flow-control - logical operators
# multiples conditionals
import os
os.system("clear")

age = 25
have_badge = True

if age >= 18 and have_badge:
    print("You can drive")
elif age >= 18 and not have_badge:
    print("You can't drive")    
elif age <= 18 and not have_badge:
    print("You can't drive")


#Javascript
# && -> and
# || -> or

# somewhre in an Island
if age >= 18 or have_badge:
    print("You can drive")
else: 
    print("Call the police!!")    
#somewhere in a country
if age >= 18 and have_badge:
    print("you can drive")
else:
    print("You can't drive call the police!!")  

is_weekend = False

if is_weekend:
    print("yeaahhh it's weekend")
if not is_weekend:
    print("Let's go work")
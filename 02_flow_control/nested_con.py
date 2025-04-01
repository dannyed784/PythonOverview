# 02 - flow-control - nested conditionals
import os
os.system("clear")

age = 20
have_money = True

if age >= 18:
    if have_money:
        print("You can get the house!!")
    else:
        print("You need to save more money")    
else:
    print("You don't have enough age to get the house")
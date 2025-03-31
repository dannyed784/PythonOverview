# 05 Basic - function input()

name = input("What is your name? ")
print(name)
print(f"Hi {name} nice to meet you!")

age = int(input("How old are you? "))
print(f"Ok so in 20 years you will be {age + 20}")

# get to variables values at the same time using split()
country, city = input("What is your country and city?\n").split()
print(f"So, your country is {country} and your city is {city}")

# Exercise 6
# Your solution comes here

a= int(input("Enter a number: "))
b= int(input("Enter another number: "))

check= "Yes" * (a % b == 0) or "No" * (a % b != 0)

print(check)
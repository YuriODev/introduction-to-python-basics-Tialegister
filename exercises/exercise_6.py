# Exercise 6
# Your solution comes here

a= int(input())
b= int(input())

check= "YES" * (a % b == 0) or "NO" * (a % b != 0)

print(check)
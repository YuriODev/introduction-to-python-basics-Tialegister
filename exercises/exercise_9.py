# Exercise 9
# Your solution comes here

h = int(input())
m = int(input())
s = int(input())
print((h % 12 * 360 + m * 360 / 60 + s * 360 / 3600) % 360)
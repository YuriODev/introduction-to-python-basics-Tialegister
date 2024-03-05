# Exercise 9
# Your solution comes here

h = int(input("Enter Hours: "))
m = int(input("Enter Minutes: "))
s = int(input("Enter Seconds: "))
print((h % 12 * 360 + m * 360 / 60 + s * 360 / 3600) % 360)
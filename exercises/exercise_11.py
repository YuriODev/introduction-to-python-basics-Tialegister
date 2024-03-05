# Exercise 11
# Your solution comes here

s = int(input("The total cost: "))
notes = [500, 100, 10, 5, 2, 1]
for note in notes:
    print(s // note, end=" ")
    s = s % note
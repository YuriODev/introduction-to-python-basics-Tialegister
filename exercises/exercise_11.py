# Exercise 11
# Your solution comes here

s = int(input())
notes = [500, 100, 10, 5, 2, 1]
for note in notes:
    print(s // note, end=" ")
    s = s % note
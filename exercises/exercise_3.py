# Exercise 3
# Your solution comes here

Time= int(input("Enter the number of seconds since midnight: "))

Hours= Time//3600
Mins = (Time%3600)//60
Secs = Time%60

print(f"{Hours}:{Mins}:{Secs}")
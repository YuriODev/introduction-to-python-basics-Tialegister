# Exercise 3
# Your solution comes here

Time= int(input())

Hours= Time//3600
Mins = (Time%3600)//60
Secs = Time%60

print(f"{Hours}:{Mins}:{Secs}")
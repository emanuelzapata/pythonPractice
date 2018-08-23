#https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

import datetime
now = datetime.datetime.now()
name = input("Enter your name:")
age = int(input("Enter your age:"))
repeat = int(input("Enter a number to repeat:"))

t = 100-age
t = now.year + t
print("Hello, "+ name)
for x in range(repeat):
    print("You will turn 100 in year: "+ str(t))

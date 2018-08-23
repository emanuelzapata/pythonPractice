#https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html


counter = int(input("How many fibonacci numbers to generate?: "))

a = 0
b = 1
for i in range(counter):
    c = a + b
    a = b
    b = c
    print(b)

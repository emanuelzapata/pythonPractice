#https://www.practicepython.org/exercise/2014/02/26/04-divisors.html

givenValue = int(input("Enter a number to check for divisors: "))
list = []
for x in range(givenValue):
    if givenValue % (x+1) == 0:
        list.append(x+1)
for i in list:
    print(i)

#https://www.practicepython.org/exercise/2014/05/28/16-password-generator.html
import random
#these three lists hold the generated ascii characters
lowerCase = [chr(i) for i in range(97,122)]
upperCase = [chr(i) for i in range(65, 90)]
characters = [chr(i) for i in range(33, 64)]
all = [lowerCase, upperCase, characters]

def generateComplexPassword(l, size):
    password = str()
    for i in range(size):
        first = random.randint(0,2)
        second = random.randint(0,len(l[first])-1)
        password = password + l[first][second]
    return password

def generateMediumPassword(l, size):
    password = str()
    for i in range(size):
        first = random.randint(0,1)
        second = random.randint(0,len(l[first])-1)
        password = password + l[first][second]
    return password

def generateSimplePassword(l, size):
    password = str()
    for i in range(size):
        first = 0
        second = random.randint(0,len(l[first])-1)
        password = password + l[first][second]
    return password


print(generateComplexPassword(all,10))
print(generateMediumPassword(all,10))
print(generateSimplePassword(all,10))

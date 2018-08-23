#https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html

def parseString(s):
    newString = s.split(" ")
    return newString

def reverseList(l):
    counter = len(l)-1
    newList = []
    while counter != -1:
        newList.append(l[counter])
        counter -=1
    return newList


t = reverseList(parseString(input("Enter a string: ")))
newString = str()
for i in t:
    newString = newString + " " + i

print(newString)

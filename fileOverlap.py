#https://www.practicepython.org/exercise/2014/12/14/23-file-overlap.html
def cleanString(s):
    s = s.strip()
    return s

def cleanListOfSpaces(list):
    for i in range(len(list)-1):
        list[i] = cleanString(list[i])
    return list

def readInFile(fileName):
    with open(fileName, 'r') as p:
        file = p.read()
    return file

def createList(list1, list2):
    temp = []
    for i in range(len(list1)-1):
        if list1[i] in list2:
            temp.append(list1[i])
    return temp

primeNumbers = readInFile('primenumbers.txt')
happyNumbers = readInFile('happynumbers.txt')

primeNumbers = cleanListOfSpaces(primeNumbers.split("\n"))
happyNumbers = cleanListOfSpaces(happyNumbers.split("\n"))

#print(createList(primeNumbers,happyNumbers))

#https://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html

def printTopBot(size):
    string = ""
    for i in range(size):
        string = string + "--- "
    return string

def printSide(size):
    string = ""
    for i in range(size):
        string = string + "|   "
    return string

#print(printTopBot(6))
#print(printSide(6))
size = int(input("Enter baord size: "))
for i in range(size):
    print(printTopBot(size))
    print(printSide(size))

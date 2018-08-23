#https://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html
import random

num = random.randint(1000,9999)
def findCows(generatedNumber, userNumber):
        cows = 0
        for i in range(4):
            if generatedNumber[i] == userNumber[i]:
                cows += 1
        return cows

def findBulls(generatedNumber, userNumber):
    bulls = 0
    for i in range(4):
        if userNumber[i] in generatedNumber:
            bulls += 1
    return bulls

def checkString(userNumber):
    if len(userNumber) == 4:
        return True
    else: return False

def __main__():
    print("Welcome to the Cows and Bulls Game!")
    while True:
        userInput = input("Enter a number: ")
        if checkString(str(userInput)) == False:
            print("Please enter a 4 digit number and try again! ")
        else:
            cows = findCows(str(num),userInput)
            bulls = findBulls(str(num),userInput)
            if bulls == 4 and cows == 4:
                print("Congratulations, you guessed the right number! ")
                break
            elif userInput.lower() == "exit":
                print("Thank you for playing, goodbye! ")
                break
            else:
                print("%s cows and %s bulls" %(cows, bulls))

__main__()

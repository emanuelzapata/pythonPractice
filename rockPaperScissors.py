#https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

keyVal = {
    "rock":3,
    "scissors":2,
    "paper":1
}

def checkForAnswerValidity(str):
    if str == "rock":
        return True
    elif str == "paper":
        return True
    elif str == "scissors":
        return True
    else: return False

def determineWinner(p1, p2):
    if keyVal[p1] > keyVal[p2]:
        return "Player 1"
    else: return "Player 2"

while True:
    playerOne = input("Player One, Enter your choice: ")
    playerTwo = input("Player Two, Enter your choice: ")
    print(determineWinner(playerOne, playerTwo))
    response = input("Play again?: ")
    if response.lower() == "no":
        break

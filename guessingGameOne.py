#https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

import random

integer = random.randint(1,10)
counter = 0
while True:
    counter +=1
    guess = input("Guess a number: ")
    if guess.lower() == "exit":
        print("Thanks for playing!!!!")
        break
    elif int(guess) > integer:
        print("Guess was too high, go lower")
    elif int(guess) < integer:
        print("Guess was too low, go higher")
    else:
        print("Congratulations, the correct number was " + str(guess) + " and you guessed: " + str(integer))
        print("You guessed a total of " +str(counter) + " times")
        integer = random.randint(1,10)

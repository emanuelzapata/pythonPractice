#https://www.practicepython.org/exercise/2015/11/01/25-guessing-game-two.html

print("Think of a number between 1-100 and I will guess it")

start = 0
end = 100
while True:
    response = input("Is your number "+str(int((start+end)/2))+"?: ")
    if response == "yes":
        break
    else:
        response = input("Was this number too high or too low?: ")
        if response.lower() == "too high":
            end = (start+end)/2
        else:
            start = (start+end)/2

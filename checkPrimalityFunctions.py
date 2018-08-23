#https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html

prime = int(input("Enter a number to check if it is prime: "))

list = [i+1 for i in range(prime) if prime %(i+1) ==0]

if len(list) == 2:
    print("The number " + str(prime) + " is prime")
else:
    print("The number " + str(prime) + " is not prime")

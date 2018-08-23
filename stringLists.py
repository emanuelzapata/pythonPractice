#https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

palindrome = input("Enter a string to check: ")

startIndex = 0
endIndex = len(palindrome)-1

while startIndex != endIndex:
    if palindrome[startIndex] == palindrome[endIndex]:
        startIndex += 1
        endIndex -=1
    else: break

if startIndex == endIndex:
    print("this is a palindrome")
else:
    print("This is not a palindrome")

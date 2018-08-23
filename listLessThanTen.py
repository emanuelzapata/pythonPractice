#https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newList = []
for i in a:
    if i <= 5:
        newList.append(i)
for i in newList:
    print(i)

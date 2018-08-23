#https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html

def removeDups(list):
    newList = set()
    for i in list:
        newList.add(i)
    return newList

t = [1, 1, 3, 4,5, 56,6,7,8,6,5,4,3,2]

print(removeDups(t))

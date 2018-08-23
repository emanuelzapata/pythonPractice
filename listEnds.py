#https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html
a = [5, 10, 15, 20, 25]

def returnList(l):
    return [l[0],l[len(l)-1]]

print(returnList(a))

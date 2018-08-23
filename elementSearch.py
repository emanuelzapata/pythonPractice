#https://www.practicepython.org/exercise/2014/11/11/20-element-search.html

list = [i for i in range(100) if i%2 ==0]
print(list)
def binarySearch(list, number):
    start = 0
    end = len(list)-1
    #center = (start+end)/2
    while True:
        center = int((start+end)/2)
        if list[center] == number:
            return True
        elif list[center] <= number:
            start = center
        elif list[center] >= number:
            end = center
        elif start == end or start > end:
            return False

def __main__():
    result = binarySearch(list, int(input("Enter a number to check if its in the list: ")))
    print(str(result))

__main__()

#import random
#from fileOverlap import readInFile
#def readInFile(fileName):
    #with open(fileName, 'r') as p:
    #    file = p.read()
    #return file

#list = readInFile("sowpods.txt")
#list = list.split("\n")

#def pickARandomWord(list):
#    return list[random.randint(0,len(list)-1)]

#print(pickARandomWord(list))
def pickARandomWord():
    import random
    from fileOverlap import readInFile

    list = readInFile("sowpods.txt")
    list = list.split("\n")

    return list[random.randint(0,len(list)-1)]

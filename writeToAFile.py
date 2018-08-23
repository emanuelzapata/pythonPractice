#https://www.practicepython.org/exercise/2014/11/30/21-write-to-a-file.html

fileName = input("Name the file to save to: ")
open_file = open(fileName+".txt", "w")
open_file.write("testing this if ti works\n")
open_file.write("is this going to be another line?")
open_file.close()

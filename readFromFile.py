#https://www.practicepython.org/exercise/2014/12/06/22-read-from-file.html

with open('nameslist.txt', 'r') as open_file:
    all_text = open_file.read()
list = all_text.split("\n")
print(len(list))
print(list)

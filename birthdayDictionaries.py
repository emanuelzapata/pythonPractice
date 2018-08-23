#https://www.practicepython.org/exercise/2017/01/24/33-birthday-dictionaries.html

birthdays = {
    "Emanuel Zapata" : "October 15, 1991",
    "Marta Garcia" : "December 12, 1967",
    "Krystal Cantu" : "October 25, 1992",
    "Jr Zapata" : "August 29, 2010"
}

print("Welcome to the birthday dictionary. We know the birthdays of:")
for key, value in birthdays.items():
    print(key)
print(birthdays[input("Who's birthday would you like?: ")])

import json

with open("birthdays.js", "r") as f:
    info = json.load(f)
print(info["Emanuel Zapata"])

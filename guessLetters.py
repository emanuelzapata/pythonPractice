from pickWord import pickARandomWord

word = pickARandomWord()
hangmanWord = ""
for i in range(len(word)-1):
    hangmanWord = hangmanWord + "_ "

print("Welcome to Hangman!")
print(hangmanWord, end='')

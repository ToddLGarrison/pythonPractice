import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""

for letter in chosen_word:
    placeholder += "_"
print(placeholder)

guess = input("Please guess a letter: \n").lower()
print(guess)

for letter in chosen_word:
    if letter == guess:
        print("right")
    else:
        print("wrong")

#create placeholder with same num blanks as letters in chosen word

#display the puts guess letter in right spot


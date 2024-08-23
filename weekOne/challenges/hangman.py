import random

word_list = ["aardvark", "baboon", "camel"]

#randomly select work
chosen_word = random.choice(word_list)
print(chosen_word)


#ask user to guess a letter, assign as variable and make lowercase
guess = input("Please guess a letter: \n").lower()
print(guess)

#check if letter guessed is one of the letters in chosen word

for letter in chosen_word:
    if letter == guess:
        print("right")
    else:
        print("wrong")
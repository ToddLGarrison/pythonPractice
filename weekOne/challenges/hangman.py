import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""

for letter in chosen_word:
    placeholder += "_"
print(placeholder)

correct_letters = []

game_over = False

lives = 6

while not game_over:
    guess = input("Please guess a letter: \n").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
            


if guess not in chosen_word:
    lives -= 1
    if lives == 0:
        game_over = True
        print("You lose!")

    print(display)

    if "_" not in display:
        print("You win!")
        game_over = True

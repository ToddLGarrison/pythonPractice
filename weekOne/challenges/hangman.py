import random

word_list = ["aardvark", "baboon", "camel"]

lives = 6
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""

for letter in chosen_word:
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"***************************{lives}/6 LIVES LEFT***************************")
    guess = input("Please guess a letter: \n").lower()

    if guess in correct_letters:
        print(f"Already guessed the letter: {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
            
    print("Word to guess: " + display)


    if guess not in chosen_word:
        lives -= 1
        print(f"Letter {guess} is not in the word")

        if lives == 0:
            game_over = True
            print("***************************YOU LOSE!***************************")

        print(display)

        if "_" not in display:
            print("***************************YOU WIN!***************************")
            game_over = True

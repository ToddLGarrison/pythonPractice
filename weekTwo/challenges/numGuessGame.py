import random

random_number = random.randint(1, 100)

def guessing_game():
    easy_or_hard_guesses = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if easy_or_hard_guesses == 'easy':
        guess_counter = 10
    else:
        guess_counter = 5

    while guess_counter > 0:
        print(f"You have {guess_counter} attempts to guess the number")
        player_guess = int(input("Make a guess: "))
        if player_guess < random_number:
            guess_counter -= 1
            print("Too low")
        elif player_guess > random_number:
            print("Too high")
            guess_counter -= 1
        elif player_guess == random_number:
            print("Correct!")
            return
    if guess_counter == 0:
        print(f"Out of attempts the correct number was {random_number}")
        return
guessing_game()
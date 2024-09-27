import random

random_number = random.randint(1, 100)

easy_guesses = 10
hard_guesses = 5

def guessing_game():
    easy_or_hard_guesses = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if easy_or_hard_guesses == 'easy':
        guess_counter = 10
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
            else:
                print("Out of attempts")
                return
    else:
        guess_counter = 5

        while guess_counter > 0:
            print(f"You have {guess_counter} attempts to guess the number")
            if player_guess < random_number:
                guess_counter -= 1
                print("Too low")
            elif player_guess > random_number:
                print("Too high")
                guess_counter -= 1
            elif player_guess == random_number:
                print("Correct!")
                return
            else:
                print("Out of attempts")
                return

guessing_game()
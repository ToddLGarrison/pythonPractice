import random

random_number = random.randint(1, 100)

print("Welcome to the guessing game!")
print("I am thinking of a number between 1 and 100, can you guess it?")

def guessing_game():
    easy_or_hard = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if easy_or_hard == 'easy':
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
        else:
            print(f"Correct! The number was {random_number}")
            return
    if guess_counter == 0:
        print(f"Out of attempts the correct number was {random_number}")
        return
guessing_game()
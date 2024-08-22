import random

print("Rock, Paper, Scissors!")

options = ["rock", "paper", "scissors"]

player_num = int(input("What do you choose? Type 0 for Rock, Type 1 for Paper, Type 2 for Scissors \n"))

comp_choice = random.randint(0, 2)
print(f"You chose {options[player_num]}")
print(f"Computer choice {options[comp_choice]}")


if player_num >= 3 or player_num < 0:
    print(f"You entered an invalid number, {player_num}. You lost")
elif player_num == 0 and comp_choice == 2:
    print("You win!")
elif comp_choice == 0 and player_num == 2:
    print("You lose!")
elif comp_choice > player_num:
    print("You lose!")
elif player_num > comp_choice:
    print("You win!")
elif comp_choice == player_num:
    print("Draw!")
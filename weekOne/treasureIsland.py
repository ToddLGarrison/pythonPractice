print("Welcome to Treasure Island")
print("Your mission is to find the treasure!")

direction = input('Do you want to go left or right? Please type "left" or "right". \n').lower()

if direction == "left":
    swim_or_wait = input('You\'ve come to a lake. Where do you want to go? ' 
        'Do you want to swim or wait for a boat? Type "swim" or "wait"\n').lower()
    if swim_or_wait == "wait":
        door_color = input('You\'ve arrive at the island unharmed. '
                            'There is a house with 3 doors. A red door, a blue door and a yellow door. '
                            'Which door do you want to enter? '
                            'Please type "red", "blue", or "yellow" \n').lower()
        if door_color == "yellow":
            print("You found the treasure! You win!")
        elif door_color == "red":
            print("You burned in a fire. Game over")
        elif door_color == "blue":
            print("Eaten by a worm. Game over")
        else:
            print("Wrong! Game Over! You lose, good day!")
    else:
        print("You were attacked by a trout. Game over")
else:
    print("You fell in a hole. Game over")


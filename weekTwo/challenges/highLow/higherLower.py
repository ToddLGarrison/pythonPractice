import random
from hlGameData import data

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def game():
    score = 0
    game_continue = True
    b = random.choice(data)

    while (game_continue):
#Generate random account from data
        a = b
        b = random.choice(data)
        if a == b:
            b = random.choice(data)
# display compare data
        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
        print("VS")
        print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}")
# Get answer input
        guess = input("Who has more followers? 'A' or 'B': ").lower()

        print('\n' * 25)

# Check if user is correct
    # get follower count
    # use if statement to check if user is correct
        a_follower_count = a['follower_count']
        b_follower_count = b['follower_count']
        
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        if is_correct:
# keep score
            score += 1
# give user feedback
            print(f"You're right! Current score: {score}")
        else:
            game_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

# Make repeatable - option b becomes option a if user correct answer


game()
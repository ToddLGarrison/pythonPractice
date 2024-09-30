import random
from hlGameData import data

def game():
    score = 0
    more_popular = {}
    game_continue = True

    while (game_continue):
#Generate random account from data
        a = random.randint(0,len(data))
        b = random.randint(0,len(data))
# display compare data
        print(f"Compare A: {data[a]['name']}, a {data[a]['description']}, from {data[a]['country']}")
        print("VS")
        print(f"Compare B: {data[b]['name']}, a {data[b]['description']}, from {data[b]['country']}")
# Get answer input
        answer = print("Who has more followers? 'A' or 'B'").lower()
# Check if user is correct
    # get follower count
    # use if statement to check if user is correct

# give user feedback

# keep score

# Make repeatable - option b becomes option a if user correct answer

import random
from hlGameData import data

# def game():
#     score = 0
#     more_popular = {}
#     game_continue = True

#     while (game_continue):


random_data = random.randint(0,len(data))

print(data[random_data]['name'])
import random


def deal_card():
    """Returns a random card from deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and calculate the score of the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

player_hand = []
comp_hand = []
player_score = -1
comp_score = -1
is_game_over = False

for _ in range(2):
    player_hand.append(deal_card())
    comp_hand.append(deal_card())

while not is_game_over:
    player_score = calculate_score(player_hand)
    comp_score = calculate_score(comp_hand)

    if player_score == 0 or comp_score == 0 or player_score > 21:
        is_game_over = True
    else:
        player_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if player_should_deal == 'y':
            player_hand.append(deal_card())
        else:
            is_game_over = True

while comp_score != 0 and comp_score < 17:
    comp_hand.append(deal_card())
    comp_score = calculate_score(comp_hand)


print(player_hand)
print(comp_hand)


print(f"Your cards: {player_hand}, current score: {player_score}")
print(f"Computer's first card: {comp_hand[0]}")
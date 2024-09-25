import random


def deal_card():
    """Returns a random card from deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

player_hand = []
comp_hand = []

for _ in range(2):
    player_hand.append(deal_card())
    comp_hand.append(deal_card())
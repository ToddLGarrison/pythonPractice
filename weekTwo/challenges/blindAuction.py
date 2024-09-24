def find_highest_bid(bidding_dictionary):
    winner = ""
    highest_bid = 0
    
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the a bid of {highest_bid} and the")

bids = {}
continue_bidding = True

while continue_bidding == True:
    name = input("What is your name? ")
    price = float(input("What is your bid $? "))
    bids[name] = price
    should_continue = input("Are there any more bidders? Type 'yes' or 'no' \n").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bid(bids)
    elif should_continue == "yes":
        print("\n" * 100)
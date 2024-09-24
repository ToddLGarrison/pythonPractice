def bid_app():
    name = input("What is your name? \n")
    price = float(input("What is your bid $? \n"))

    bids = {}
    bids[name] = price

    should_continue = input("Are there any more bidders? Type 'yes' or 'no' \n").lower()
    
    continue_bidding = False

    if should_continue == 'yes':
        continue_bidding = True

    while continue_bidding == True:
        print("\n" * 20)
        bid_app()
    else:
        for bidder in bids:
            highest_bidder = {}
            if(bidder[price] > highest_bidder):
                highest_bidder = {bidder["name"], bidder["price"]}
            return highest_bidder
    
    print(f"bids", bids)


bid_app()
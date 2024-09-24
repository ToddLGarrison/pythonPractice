def bid_app():
    additional_bidder = False
    
    name = input("What is your name? \n")
    price = float(input("What is your bid $? \n"))

    bids = {}
    bids[name] = price

    more_bidder = input("Are there any more bidders? Type 'yes' or 'no' \n").lower()
    
    if(more_bidder == 'yes'):
        additional_bidder = True
        if(bidder_dictionary == True):
            print("\n" * 20)
            bid_app()
        else:
            for bidder in bidder_dictionary:
                highest_bidder = {}
                if(bidder[price] > highest_bidder):
                    highest_bidder = {bidder["name"], bidder["price"]}
                return highest_bidder
    
    print(f"bidder dictionary", bidder_dictionary)


bid_app()
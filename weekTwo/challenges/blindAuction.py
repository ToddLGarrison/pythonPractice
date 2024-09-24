def bid_app():
    bidder_dictionary = {}
    additional_bidder = False
    
    name = input("What is your name? \n")
    bid_amount = input("What is your bid amount? \n")

    bidder_dictionary = {
        "name": name,
        "bid_amount": bid_amount,
    }

    more_bidder = input("Are there any more bidders? 'Yes' or 'No' \n").lower()
    
    if(more_bidder == 'yes'):
        additional_bidder = True
        if(bidder_dictionary == True):
            bid_app()
        else:
            for bidder in bidder_dictionary:
                highest_bidder = {}
                if(bidder[bid_amount] > highest_bidder):
                    highest_bidder = {bidder["name"], bidder["bid_amount"]}
                return highest_bidder
    
    print(f"bidder dictionary", bidder_dictionary)


bid_app()
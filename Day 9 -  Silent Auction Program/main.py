print("Greetings! Welcome to the Silent Auction Program")

auction_on = True

auction_dictionary = {}

max_bid = {}

while auction_on == True:
    name = input("What is your name? :  ")
    bidding_amount = int(input("What's your bid? :  $"))

    auction_dictionary[name] = bidding_amount

    more_players = input("Are there more players? Type 'yes' or 'no': ").lower()

    if more_players == "yes":
        auction_on = True
    else:
        auction_on = False


def find_highest_bidder(auction_dictionary):
    winner = ""
    highest_bid = 0
    for name in auction_dictionary:
        bid_amount = auction_dictionary[name]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = name

    print(f"The winner is {winner} with a bid of ${highest_bid}")

find_highest_bidder(auction_dictionary=auction_dictionary)

# Simpler approach - 
# print(f"The winner is {max(auction_dictionary, key=auction_dictionary.get)} with a bid of ${max(auction_dictionary.values())}")
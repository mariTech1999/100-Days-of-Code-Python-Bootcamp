import art

def find_winner(bids):
    biggest_bid = 0
    winner_name = ""

    for name in bids:
        price = bids[name]
        if price > biggest_bid:
            biggest_bid = price
            winner_name = name

    print(f"The winner is {winner_name} with a bid of ${biggest_bid}")



print(art.logo)

bids = {}

bidding = True

while bidding:
    name = input("What's your name?: ")
    price = int(input("What's your bid?: R$"))

    bids[name] = price

    more_bidders = input("There are more bidders?\nType 'yes' or 'no': ")
    if more_bidders == "no":
        find_winner(bids)
        bidding = False
    else:
        print("\n" * 30)
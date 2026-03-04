from art import logo

def decide_winner():
    max_bid = max(bids.values())
    for bidder in bids:
        if bids[bidder] == max_bid:
            winner = bidder
    print(f"The winner of the auction is {winner} with the bid of ${max_bid} dollars.")

bids = {}

print(logo)
print("Welcome to the bling auction program")

more_bidders = 'yes'

while more_bidders == 'yes':

    name = input("Please enter the name for the bid\n")
    bid = int(input("Please enter the price to bid\n"))

    bids[name] = bid
    print("Your bid is stored...")

    more_bidders = input('Are there are more bidders? (yes/no)\n')

    if more_bidders == 'yes':
        import os
os.system('cls')  # Windows

decide_winner()

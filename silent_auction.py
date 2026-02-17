from auction_art import logo
def highest_bidder(participaters):
    highest_bid = 0
    winner = ""
    for participant in participaters:
        if participaters[participant] > highest_bid:
            highest_bid = participaters[participant]
            winner = participant
    return winner, highest_bid
    
participaters = {}
bids_finished = False
while not bids_finished:
    #priniying the logo
    print(logo)
    print("Welcome to the secret auction program.")
    
    #takng the input from the user and bidding amount
    name = input("what's your name?: ")
    bid = int(input("Whats's your bid: $"))

    #storing the nama and bid into dictionary
    participaters[name] = bid
    should_continue = input("Are ther any other bidders? Type 'yes' or 'no'.")

    if should_continue == "no":
        bids_finished = True
        winner, highest_bid = highest_bidder(participaters)
        print(participaters)
        print(f"The winner is {winner} with a bid of ${highest_bid}")
    elif should_continue == "yes":
        print("\n" * 10)
    else:
        None
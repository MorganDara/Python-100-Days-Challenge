from os import system
HAMMER_IMG = """
"""

auction_data = dict()

def main():
    print(HAMMER_IMG, end="\n\n")
    loop = True
    while loop:
        name = input("What is your name ?: ")
        bid = int(input("What is your bid?: $"))
        auction_data[name] = bid

        ask = input("Are they other bidders? Type 'yes' or 'no'.\n")
        loop = (ask == "yes")
        system("cls")

    winner, max_bid = "", 0
    for bidder, bid in auction_data.items():
        if bid >= max_bid:
            winner, max_bid = bidder, bid

    print(f"\nThe winner is {winner} with a bid of ${max_bid}\n")

if __name__=="__main__":
    main()
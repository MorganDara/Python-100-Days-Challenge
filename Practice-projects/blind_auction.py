'''
    Author: DARA Morgan
    Date: 16/10/2021
    Version: 1.0.0
    Description: Simple program that mimics a silent auction
'''
from os import system
HAMMER_IMG = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


auction_data = dict()

def main():
    print(HAMMER_IMG, end="\n\n")
    auction_not_finished = True
    while auction_not_finished:
        name = input("What is your name ?: ")
        bid = int(input("What is your bid?: $"))
        auction_data[name] = bid

        ask = input("Are they other bidders? Type 'yes' or 'no'.\n")
        auction_not_finished = (ask == "yes")
        system("cls")

    winner, max_bid = "", 0
    for bidder, bid in auction_data.items():
        if bid >= max_bid:
            winner, max_bid = bidder, bid

    print(f"\nThe winner is {winner} with a bid of ${max_bid}\n")

if __name__=="__main__":
    main()
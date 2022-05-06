from replit import clear

logo = '''
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

def find_the_winner(bids_records):
    highest_bid = 0
    for name in auction_bids:
      if auction_bids[name] > highest_bid:
        highest_bid = auction_bids[name]
        winner_name = name
    print(f"The winner is {winner_name} with the bid of ${highest_bid}.")

print(logo)
auction_on = True
auction_bids = {}

while auction_on:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  auction_bids[name] = bid
  other_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if other_bidder == "no":
    auction_on = False
    find_the_winner(auction_bids)
  else:
    clear()

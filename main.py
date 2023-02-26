from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
print("Welcome to the secret auction program!!")

more_auctioner = True
bids = {}

def add_bidders(bidder_name,bid_value):
  bids[bidder_name] = bid_value

def highest_bidder(bids):
  highest_bid = 0
  highest_bidder = ""
  for name in bids:
    if bids[name] > highest_bid:
      highest_bid = bids[name]
      highest_bidder = name
    
  return "The winner is " + highest_bidder + " with a bid of $" + str(highest_bid)
  
while more_auctioner == True:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  morebid = input("Are there any other bidders? Type 'yes' or 'no': ")
  add_bidders(name,bid)
  clear()
  if morebid == "no":
    more_auctioner = False
  
print(highest_bidder(bids))
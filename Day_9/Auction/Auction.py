import clear
from art import logo

print(logo)


dic1 = {}
names = []

def add():
  name = input('What is your name? ')
  bid = input('What is your bid? ')

  dic1[name] = bid
  clear()

add()


high_bid = 0
for i in range(1000):
  other_bidder = input('Are there any other bidders? ').lower()
  if other_bidder == 'no':
      for key in dic1:
          value = int(dic1[key])
          if value > high_bid:
            high_bid = value
            name = key
      print(f'{name} is the winner with a bid of {high_bid} ')
      break
  elif other_bidder == 'yes':
    add()
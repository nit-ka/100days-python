# Blackjack game

import random
from replit import clear
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
  
def deal_card(list_name):
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  list_name.append(card)

def total_score(list_name):
  score = 0
  for item in list_name:
    item = int(item)
    score += item
  if "11" in list_name and score > 21:
    score -= 10
  return score

def start_game():
  game_on = True
  clear()
  print(logo)  
  users_cards = []
  computers_cards = []

  for i in range(2):
    deal_card(users_cards)
    deal_card(computers_cards)

  # Checking for blackjack
  if total_score(computers_cards) == 21:
    game_on = False
    print(f"""Your cards: {users_cards}, current_score: {total_score(users_cards)}\nComputers cards: {computers_cards}\nComputer has a blackjack. You lose.""")
  elif total_score(users_cards) == 21:
    game_on = False
    print(f"""Your cards: {users_cards}, current_score: {total_score(users_cards)}\nComputers cards: {computers_cards}\nYou have a blackjack. You win!""")
  # No blackjack, game continues
  while total_score(users_cards) < 21 and game_on:
    print(f"""Your cards: {users_cards}, current_score: {total_score(users_cards)}\nComputer's first card: [{computers_cards[0]}] """)
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if another_card == 'y':
      deal_card(users_cards)
    elif another_card == 'n':
      game_on = False
      while total_score(computers_cards) < 17:
        deal_card(computers_cards)
      if total_score(computers_cards) > 21:
        print(f"""Your final cards: {users_cards}, final score: {total_score(users_cards)}\nComputers final cards: {computers_cards}, final score: {total_score(computers_cards)}\nComputer went over. You win!""")
      elif total_score(computers_cards) == 21:
        print(f"""Your final cards: {users_cards}, final score: {total_score(users_cards)}\nComputers final cards: {computers_cards}, final score: {total_score(computers_cards)}\nYou lose!""")
      else:
        if total_score(computers_cards) > total_score(users_cards):
          print(f"""Your final cards: {users_cards}, final score: {total_score(users_cards)}\nComputers final cards: {computers_cards}, final score: {total_score(computers_cards)}\nYou lose!""")
        elif total_score(computers_cards) == total_score(users_cards):
          print(f"""Your final cards: {users_cards}, final score: {total_score(users_cards)}\nComputers final cards: {computers_cards}, final score: {total_score(computers_cards)}\nDraw!""")
        else:
          print(f"""Your final cards: {users_cards}, final score: {total_score(users_cards)}\nComputers final cards: {computers_cards}, final score: {total_score(computers_cards)}\nYou win!""")
    
  if total_score(users_cards) == 21 and game_on:
    print(f"""Your final cards: {users_cards}, final score: {total_score(users_cards)}\nComputers final cards: {computers_cards}, final score: {total_score(computers_cards)}\nYou win!""")
  elif total_score(users_cards) > 21 and game_on:
    print(f"""Your final cards: {users_cards}, final score: {total_score(users_cards)}\nComputers final cards: {computers_cards}, final score: {total_score(computers_cards)}\nYou went over. You lose!""")
    
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  start_game()
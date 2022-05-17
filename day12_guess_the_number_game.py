# Guess the number game

import random
from replit import clear

logo = """                                                                    
 _____                    _   _                        _           
|   __|_ _ ___ ___ ___   | |_| |_ ___    ___ _ _ _____| |_ ___ ___ 
|  |  | | | -_|_ -|_ -|  |  _|   | -_|  |   | | |     | . | -_|  _|
|_____|___|___|___|___|  |_| |_|_|___|  |_|_|___|_|_|_|___|___|_|  
"""
def guess_the_number():                                                                  
  print(logo)
  print("I'm thinking of a number between 1 and 100.")
  secret_number = random.randint(1, 100)
  # print(f"The secret number is: {secret_number}")
  
  difficulty = input("Choose a difficulty level. Type 'easy' or 'hard': ")
  if difficulty == 'easy':
    guesses_left = 10
  elif difficulty == 'hard':
    guesses_left = 5
  else:
    print("Invalid input. Try again.")
  guessed_number = 0
  
  while guessed_number != secret_number and guesses_left > 0:
    if guesses_left > 1:
      print(f"You have {guesses_left} attempts remaining to guess the number.")
    elif guesses_left == 1:
      print(f"You have {guesses_left} attempt remaining to guess the number.")
    guessed_number = int(input("Make a guess: "))
    guesses_left -= 1
    if guessed_number > secret_number:
      print("Too high.")
    elif guessed_number < secret_number:
      print("Too low.")
    if guesses_left > 0 and guessed_number != secret_number:
      print("Guess again.")
  
  if guessed_number == secret_number:
    print("That's the number. You win!")
  elif guesses_left == 0:
    print(f"You ran out of tries. You lose. The secret number was {secret_number}.")

guess_the_number()

next_game = input("Do you want to play again? Type 'yes' or 'no': ")
if next_game == 'yes':
  clear()
  guess_the_number()

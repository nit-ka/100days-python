import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

users_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if users_choice < 0 or users_choice >= 3:
  print("You typed invalid number. You lose.")
else:
  print(game_images[users_choice])
  
  computers_choice = random.randint(0, 2)
  print(game_images[computers_choice])
  
  if users_choice == computers_choice:
    print("Draw")
  elif users_choice == 0 and computers_choice == 1:
    print("You lose")
  elif users_choice == 0 and computer_choice == 2:
    print("You win")
  elif users_choice == 1 and computers_choice == 0:
    print("You win")
  elif users_choice == 1 and computers_choice == 2:
    print("You lose")
  elif users_choice == 2 and computers_choice == 0:
    print("You lose")
  elif users_choice == 2 and computers_choice == 1:
    print("You win")
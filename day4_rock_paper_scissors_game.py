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

users_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if users_choice == 0:
  print(rock)
elif users_choice == 1:
  print(paper)
elif users_choice == 2:
  print(scissors)
  
computers_choice = random.randint(0, 2)

if computers_choice == 0:
  print(f"Computer chose:\n{rock}")
elif computers_choice == 1:
  print(f"Computer chose:\n{paper}")
elif computers_choice == 2:
  print(f"Computer chose:\n{scissors}")

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

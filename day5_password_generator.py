import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
easy_or_hard = input("Do you want to mix the order of characters in order to increase the safety of your password? Type 'y' for yes and 'n' for no.\n")

password = ""
for letter in range(0, nr_letters):
  password += random.choice(letters)
for symbol in range(0, nr_symbols):
  password += random.choice(symbols)
for number in range(0, nr_numbers):
  password += random.choice(numbers)
  
if easy_or_hard == "n":   
  print(f'''Your password is "{password}".''')
  
elif easy_or_hard == 'y':

  hard_password = ""
  no_of_characters = nr_letters + nr_symbols + nr_numbers
  list_of_char = list(password)
  
  for character in range (0, no_of_characters):
    random_char = random.choice(list_of_char)
    hard_password += random_char
    list_of_char.remove(random_char)
  
  print(f'''Your hard password is "{hard_password}".''')

else:
  print("You've typed a wrong letter. Try again.")
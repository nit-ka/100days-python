print("Welcome to Treasure Island Game.")
print("Your mission is to find the treasure.") 

decision1 = input('''You've just got to the beach of the Treasure Island. What do you want to do? Type "t" to look for a tresure or type "s" to stay on the beach and sunbathe.\n''')
if decision1 == "t":
  decision2 = input('''Great! The adventure just begins. Where do you want to start your searching? Type "j" for the jungle or "s" for the pirate ship.\n''')
  if decision2 == "j":
    decision3 = input('''You are in the middle of the jungle. You notice a lion. Type "run" to escape or "pet" to pet a lion.\n''')
    if decision3 == "pet":
      decision4 = input('''The lion turned out to be very friendly. After a while you followed him and he got you to the statue of Father Lion. Behind it you can see three caves. In which do you start to search for the tresure? Type "1" for the first from the left, "2" for second and "3" for third.\n''')
      if decision4 == "1":
        print('''You find an old library and you start reading books there. You forget about the treasue. Somevody finds it before you. Game over!''')
      elif decision4 == "2":
        decision5 = input('''You are so brave. You decided to look for a tresure, pet a lion and get into the darkest cave. It was worth it! You found a tresure! You win. Do you want to know what your treasure is? Type "y" for yes or "n" for no.\n''')
        if decision5 == "y":
          print('''Here it is. kinga.nit@gmail.com --> It's your future empoleyee's email address. Give her a chance and get her for the job interview! You have already made so many good decicions, make one more :).''')
        elif decision5 == "n":
          print('''Too bad. Now you will never know. But maybe it's the adventure, good fun and being kind to others, which is more important than the treasure?''')
        else:
          print('''Seriously? You can't type correctly "y" or "n"? How  did you win this game? You need to give the treasure back!''')
      elif decision4 == "3":
        print('''You get lost inside a cave. Fortunately the lion helps you to get out. Unfortunetaly the treasure was already found by someone else. Game over.''')
      else:
        print("Incorrect input. If you can't type the digit correctly, there's no way you will find a treasure. Game over!")
    elif decision3 == "run":
      print("You are so afraid and you are running so fast that you don't notice a giant whole in the ground. You fell into it and can't get out. You die from starvation few days later. Game over!")
    else:
      print("Incorrect input. If you can't type the letter or word correctly, there's no way you will find a treasure. Game over!")        
  elif decision2 == "s":
    print('''You started to look for a treasure in the pirate ship. Unfortunately you have only found a little hungry chichuachua "Jack", which jumped to your neck and bit through your artery. Game over!''')
  else:
    print("Incorrect input. If you can't type the letter or word correctly, there's no way you will find a treasure. Game over!")
elif decision1 == "s":
  print("The shark just jumped out of the water and ate you while you were sunbathing. Game over!")
else:
  print("Incorrect input. If you can't type the letter or word correctly, there's no way you will find a treasure. Game over!")

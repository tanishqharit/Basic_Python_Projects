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

# GAME RULES:
# Rock wins against scissors.
# Scissors wins against paper.
# Paper wins against rock.

game_images = [rock, paper, scissors]

print("What do you choose?")
user_choice = int(input("Type 0 for Rock, 1 for Paper and 2 for Scissors\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print(f"Computer chose: ")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:       # edge case
    print("Wrong command, restart game.")
if user_choice == 0 and computer_choice == 2:   # user: rock and computer: scissor
    print("You win!")
if user_choice == 2 and computer_choice == 0:   # user: scissor and computer: rock
    print("You lose!")
if user_choice > computer_choice:
    print("You win!")
if user_choice < computer_choice:
    print("You lose!")
if user_choice == computer_choice:
    print("Draw.")
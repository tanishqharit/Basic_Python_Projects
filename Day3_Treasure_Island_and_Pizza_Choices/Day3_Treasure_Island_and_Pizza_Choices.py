"""
Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.
Based on a user's order, work out their final bill.
Small pizza (S): $15
Medium pizza (M): $20
Large pizza (L): $25
Add pepperoni for small pizza (Y or N): +$2
Add pepperoni for medium or large pizza (Y or N): +$3
"""

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# My approach
bill = 0
small_pizza_price = 15
medium_pizza_price = 20
large_pizza_price = 25
small_pepperoni_price = 2
mediumOrLarge_pepperoni_price = 3
extra_cheese_price = 1

if size == "S":
    if pepperoni == "Y":
        if extra_cheese == "Y":     # wants everything
            bill = small_pizza_price + small_pepperoni_price + extra_cheese_price
            print(f"Your final bill is: ${bill}.")
        else:   # no extra cheese, but want pepperoni
            bill = small_pizza_price + small_pepperoni_price
            print(f"Your final bill is: ${bill}.")
    else:   # no pepperoni
        if extra_cheese == "Y":     # but want cheese
            bill = small_pizza_price + extra_cheese_price
            print(f"Your final bill is: ${bill}.")
        else:   # no pepperoni and no cheese
            bill = small_pizza_price
            print(f"Your final bill is: ${bill}.")
if size == "M":
    if pepperoni == "Y":
        if extra_cheese == "Y":     # wants everything
            bill = medium_pizza_price + mediumOrLarge_pepperoni_price + extra_cheese_price
            print(f"Your final bill is: ${bill}.")
        else:   # no extra cheese, but want pepperoni
            bill = medium_pizza_price + mediumOrLarge_pepperoni_price
            print(f"Your final bill is: ${bill}.")
    else:   # no pepperoni
        if extra_cheese == "Y":     # but want cheese
            bill = medium_pizza_price + extra_cheese_price
            print(f"Your final bill is: ${bill}.")
        else:   # no pepperoni and no cheese
            bill = medium_pizza_price
            print(f"Your final bill is: ${bill}.")
if size == "L":
    if pepperoni == "Y":
        if extra_cheese == "Y":     # wants everything
            bill = large_pizza_price + mediumOrLarge_pepperoni_price + extra_cheese_price
            print(f"Your final bill is: ${bill}.")
        else:   # no extra cheese, but want pepperoni
            bill = large_pizza_price + mediumOrLarge_pepperoni_price
            print(f"Your final bill is: ${bill}.")
    else:   # no pepperoni
        if extra_cheese == "Y":     # but want cheese
            bill = large_pizza_price + extra_cheese_price
            print(f"Your final bill is: ${bill}.")
        else:   # no pepperoni and no cheese
            bill = large_pizza_price
            print(f"Your final bill is: ${bill}.")

# Instructor's Approach
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You typed the wrong inputs.")

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is {bill}")

"""
Sample user inputs and outputs

Welcome to Python Pizza Deliveries!
What size pizza do you want? S, M or L: L
Do you want pepperoni on your pizza? Y or N: N
Do you want extra cheese? Y or N: Y
Your final bill is: $26.
"""
######################################################## FINAL PROJECT
print()     # For console spacing

"""
Your goal today is to build a "Chose your own adventure game".
"""

# My approach
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("You're at cross road. Where do you want to go?")
decision1 = input("Type 'left' or 'right'?\n").lower()
if decision1 == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    decision2 = input("Type 'wait' to wait for the boat or type 'swim' to swim across.\n").lower()
    if decision2 == "wait":
        print("You've arrived at the island unharmed. There is a house with three doors.")
        decision3 = input("One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if decision3 == "yellow":
            print("Room full of GOLD.You Win!")
        elif decision3 == "red":
            print("Room full of fire. Game Over.")
        elif decision3 == "blue":
            print("Room full of beasts. Game Over.")
        else:
            print("Wrong Command, restart game.")
    elif decision2 == "swim":
        print("Crocodiles. Game Over.")
    else:
        print("Wrong Command, restart game.")
elif decision1 == "right":
    print("You fell into the whole. Game Over.")
else:
    print("Wrong Command, restart game.")

"""
Sample user inputs and outputs

Case1: 
Welcome to Treasure Island.
Your mission is to find the treasure.
You're at cross road. Where do you want to go?
Type 'left' or 'right'?
right
You fell into the whole. Game Over.

Case2: 
Welcome to Treasure Island.
Your mission is to find the treasure.
You're at cross road. Where do you want to go?
Type 'left' or 'right'?
left
You've come to a lake. There is an island in the middle of the lake.
Type 'wait' to wait for the boat or type 'swim' to swim across.
wait
You've arrived at the island unharmed. There is a house with three doors.
One red, one yellow and one blue. Which colour do you choose?
yellow
Room full of GOLD.You Win!
"""

# To create these projects, following Python concepts were used:
# Control flow with if-else and conditional operators.
# Modulo Operator, Nesting and Elif statements.
# Multiple if statements.
# Python Logical Operators.
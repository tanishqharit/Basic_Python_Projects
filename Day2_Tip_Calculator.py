"""
We're going to build a tip calculator.
If the bill was $150.00, split between 5 people, with 12% tip.
Each person should pay:
(150.00 / 5) * 1.12 = 33.6
After formatting the result to 2 decimal places = 33.60
"""

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

bill_with_tip = (tip / 100 * bill) + bill
bill_per_person = bill_with_tip / people
print(round(bill_per_person, 2))

"""
Sample user inputs and outputs

Welcome to the tip calculator!
What was the total bill? $176
What percentage tip would you like to give? 10 12 15 15
How many people to split the bill? 7
28.91
"""

# To create this project, following Python concepts are used:
# Python primitive data types.
# Python datatype error, checking and conversion.
# Mathematical Operations in Python.
# Number Manipulation and f-Strings in python.
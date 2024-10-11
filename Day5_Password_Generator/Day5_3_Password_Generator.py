import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
           't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# EASY LEVEL - generating password in a sequential order (letters, numbers and symbols)

# password = ""       # variable to store password
# for char in range(0, nr_letters):
#     random_char = random.choice(letters)
#     password = password + random_char
#
# for char in range(0, nr_symbols):
#     random_char = random.choice(numbers)
#     password = password + random_char
#
# for char in range(0, nr_numbers):
#     random_char = random.choice(symbols)
#     password = password + random_char
#
# print(password)     # final password


# HARD LEVEL - generating password in a random order
# instead of storing password as a string, now we need to store password as list.
password_list = []
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

for char in range(0, nr_symbols):
    password_list.append(random.choice(numbers))

for char in range(0, nr_numbers):
    password_list.append(random.choice(symbols))

print(password_list)
random.shuffle(password_list)       # shuffling the list items, to create a random sequence

password = ""
for char in password_list:
    password += char
print(f"Your password is {password}")

"""
Sample Case: 

Welcome to the PyPassword Generator!
How many letters would you like in your password?
2
How many symbols would you like?
2
How many numbers would you like?
2
['p', 'W', '5', '4', '+', '*']
Your password is *+p5W4
"""
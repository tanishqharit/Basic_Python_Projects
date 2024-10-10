
# generating random numbers between 1 and 10.
import random
random_integer = random.randint(1, 10)
print(random_integer)

# generating random numbers between 0 and 1.
random_number_between_0_and_1 = random.random()
print(random_number_between_0_and_1)
# going to be between 0 (inclusive) and 1 (non-inclusive)

random_float = random.uniform(1, 10)
print(random_float)
# going to be floats between 1 (inclusive) and 10 (inclusive)

# Heads and Tails program
heads_or_tails = random.randint(0, 1)
if heads_or_tails == 0:
    print("Tails")
else:
    print("Heads")
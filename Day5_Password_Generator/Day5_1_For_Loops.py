# A list of fruits
fruits = ["Apple", "Banana", "Peach"]

for fruit in fruits:        # fruit is a variable, in which each element of list "fruits" is assigned.
    print(fruit)            # then each element is printed by looping through list until the end.
print(fruits)           # outside the loop.

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# Python sum functionality
print(sum(student_scores))

# Creating sum functionality using for loop
Sum = 0     # sum container
for score in student_scores:
    Sum += score       # Sum = Sum + Scores
print(Sum)

print(max(student_scores))      # giving the maximum number (highest score)

# Creating this functionality
print("Maximum Score")
max_score = 0                   # container for maximum score
for score in student_scores:    # looping through each score (element).
    if score > max_score:       # if element1 (150) > max_score -> true -> max_score = 150
        max_score = score       # similar will happen with each and every element.
print(max_score)                # finally, maximum score will be printed.

# Creating the min functionality
print("Minimum Score")
min_score = max_score               # we assigned min_score = max_score, because here, we are doing it reverse
for score in student_scores:        # high values will be compared
    if score < min_score:           # if element1(150) < min_score (max_score = 199) -> min_score = 150
        min_score = score           # if element2(142) < min_score (150) -> min_score = 142 ......
print(min_score)                    # if we put min_score = 0, then 0 will be printed as 0 is the minimum number.

# Add all numbers 1 to 100 - using range() function
print("Sum of numbers from 1 to 100")
total = 0
for number in range(1, 101):    # from 1 to 101 (101 non-inclusive)
    total += number
print(total)

# Skipping numbers using step - printing all odd numbers
print("Odd numbers")
for number in range (1, 10, 2):     # range (1, 10) and step = 2
    print(number)

# Similarly, printing all even numbers
print("Even numbers")
for number in range(0, 10, 2):      # range (0, 10) and step = 2
    print(number)

"""
Console Output

Apple
Banana
Peach
['Apple', 'Banana', 'Peach']
2068
2068
199
Maximum Score
199
Minimum Score
24
Sum of numbers from 1 to 100
5050
Odd numbers
1
3
5
7
9
Even numbers
0
2
4
6
8
"""

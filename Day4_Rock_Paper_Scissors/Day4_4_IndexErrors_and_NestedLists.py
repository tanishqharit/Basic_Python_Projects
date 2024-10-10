states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]

# length of list
print(len(states_of_america))

# if we try to access elements outside this length, we will get an error
# print(states_of_america[50])
# This is wrong, because range is from 0 to 49.

# 2 list of fruits and vegetables
fruits = ["apple", "banana", "orange", "strawberry"]
vegetables = ["onion", "tomato", "spinach", "potato"]
# combining these lists
combined = [fruits, vegetables]
print(combined)

"""
On console: 

50
[['apple', 'banana', 'orange', 'strawberry'], ['onion', 'tomato', 'spinach', 'potato']]
"""
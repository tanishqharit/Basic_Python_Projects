# Picking a random name from the list of friends.

import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Approach 1
random_index = random.randint(0, 4)
print(friends[random_index])

# Approach 2 - Using "choice"
print(random.choice(friends))
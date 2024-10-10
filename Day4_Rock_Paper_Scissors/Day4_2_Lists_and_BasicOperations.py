
# List is a data structure (way of organising and storing data) in python.
# Variables can store single pieced data and data structures can hold grouped pieces of data.

# A list of strings
states_of_america = ["California", "Massachusetts", "New Jersey", "New York", "Pennsylvania", "Delaware"]
print(states_of_america)

# Accessing elements from a list (list index starts from 0)
print(states_of_america[0])
print(states_of_america[1])
print(states_of_america[3])
# Accessing from backwards
print(states_of_america[-1])
print(states_of_america[-2])

# Refactoring existing elements in the list
states_of_america[3] = "Concrete Jungle"
print(states_of_america)

# Appending elements (will append a single item to the list)
states_of_america.append("Florida")
print(states_of_america)

# Extending the list - append multiple elements
states_of_america.extend(["Arizona", "Nevada", "Illinois"])
print(states_of_america)

"""
On console: 

['California', 'Massachusetts', 'New Jersey', 'New York', 'Pennsylvania', 'Delaware']
California
Massachusetts
New York
Delaware
Pennsylvania
['California', 'Massachusetts', 'New Jersey', 'Concrete Jungle', 'Pennsylvania', 'Delaware']
['California', 'Massachusetts', 'New Jersey', 'Concrete Jungle', 'Pennsylvania', 'Delaware', 'Florida']
['California', 'Massachusetts', 'New Jersey', 'Concrete Jungle', 'Pennsylvania', 'Delaware', 'Florida', 'Arizona', 'Nevada', 'Illinois']
"""
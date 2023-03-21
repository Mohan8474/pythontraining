# from present import init
# init()
import random

# Create an empty list
my_list = []

# Generate 10 random integers and add them to the list
for i in range(10):
    my_list.append(random.randint(1, 100))

print("Random integers:", my_list)

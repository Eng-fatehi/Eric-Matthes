'''
# import random module 
import random

# Define roll_die() function
def roll_die():
    return random.randint(1, 6) # Return a random integer between 1 and 6

# Simulate rolling the die 5 times
for i in range(5):
    result = roll_die()
    print(f"Roll {i+1}: {result}") # function

    # randint is a function that returns a random integer
    # random is a module that contains the randint() function

    '''
# Import random module and define roll_die() function
import random

def roll_die():
    return random.randint(1, 6)

# Simulate rolling the die 5 times
for i in range(5):
    result = roll_die()
    print(result)
    print(f"Roll {i+1}: {result}")


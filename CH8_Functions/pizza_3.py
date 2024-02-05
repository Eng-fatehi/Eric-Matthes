""" Print the list of toppings that have beern requested."""
""" Summarize the pizza we are about to make. """
""" Mixing Positonal and variable number of argumens"""
# replace the print() call with a loop that runs through the list of toppings and desribes the pizza being ordered.
def make_pizza(size, *toppings):   # a variable number of arguments must be placed last in the function defination.
    print(f"\nMaking a {size}-inch pizza with the fllowing toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')

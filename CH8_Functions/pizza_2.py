""" Print the list of toppings that have beern requested."""
""" Summarize the pizza we are about to make. """
# replace the print() call with a loop that runs through the list of toppings and desribes the pizza being ordered.
def make_pizza(*toppings):   
    print("\nMaking a pizza with the fllowing toppings:")
    for topping in toppings:
        print(f"- {topping}")  

make_pizza('pepperoni')
make_pizza('mushroom', 'green peppers', 'extra cheese')
make_pizza('mu', 'gr peppers', 'eeese')
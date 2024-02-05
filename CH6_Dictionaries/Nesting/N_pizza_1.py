''' A List in a Dictionaty. '''

# Example 1: Pizza
# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',                                     # crust قشره
    'toppings': ['mushrooms', 'extra cheese'],
}

# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")  # \t used toadds a tab( 4 spaces ) to each line.
""" Passing an Arbitraty (A variable) number of Arguments. """
""" Print the list of toppings that have beern requested."""
def make_pizza(*toppings):   # * the asterisk in the parameter tells Python to make a tuple ('a', 'b', 'c') 
    print(toppings)          #containing all the values.

make_pizza('pepperoni')
make_pizza('mushroom', 'green peppers', 'extra cheese')
 

 # this syntax works no matter how many arguments the function receives.
 # more example of a variable (arbitrary) number of arguments:
 # https://www.youtube.com/watch?v=IhrAFOiRhYc
 # https://www.youtube.com/watch?v=f2HjpuPpGrk
 # https://www.youtube.com/watch?v=QpKrOph23Uw
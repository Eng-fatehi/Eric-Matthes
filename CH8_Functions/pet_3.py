""" Display information about a pet."""
#Default Values

def describe_pet(pet_name, animal_type='dog'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')


#The parameter and argument can be used for the same thing: information that are passed into a function. 
#From a function's perspective: 
#A parameter is the variable listed inside the parentheses in the function definition. 
#An argument is the value that are sent to the function when it is called.
#Python uses the argument value. If not, It uses the parameter's default value.
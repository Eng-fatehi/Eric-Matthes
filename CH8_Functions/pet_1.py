""" Positional Argument: based on the order of the arguments. """
""" Display information about a pet."""
def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')

#f string:
#print(f"I have a {animal_type}.")
#print(f"My {animal_type}'s name is {pet_name.title()}.")

#normal string:
#print("I have a "+animal_type+".")
#print("My "+animal_type+"'s name is "+pet_name.title()+".")
""" Display information about a pet."""
#Keyword Arguments

def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type="hamster", pet_name="harry")


#Keyword Arguments
#you directly associate the name and the value within the argument, there's no confusion. 
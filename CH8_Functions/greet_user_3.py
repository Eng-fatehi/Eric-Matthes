""" Return full name, neatly formatted. """
def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}" 
    return full_name.title()
#This is an infinite loop!
while True:
    print("\nPleas tell my your name:")
    f_name = input("first_name:")
    l_name = input("last_name:") 

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
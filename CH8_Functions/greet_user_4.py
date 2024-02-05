""" Return full name, neatly formatted. """
def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}" 
    return full_name.title()
#This is not infinite loop!
while True:
    print("\nPleas tell my your name:")
    print("(enter 'q' at any time to quite)")

    f_name = input("first_name:")
    if f_name == 'q':
        break

    l_name = input("last_name:") 
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
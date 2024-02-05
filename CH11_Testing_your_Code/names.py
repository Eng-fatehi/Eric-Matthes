from name_function_1 import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:                                         # while loop is used to run the program until the user types q.
    first = input("\nPlease give me a first name:") # input() function is used to get user input.
    if first == 'q':                                # if the user types q, the program will exit.
        break                                       # break is used to exit the loop.
    last = input("Please give me a last name:")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")






""" 
def get_formatted_name(first, last):            # get formatted name function used to return full name.
    full_name = f"{first} {last}"               
    return full_name.title()
 """

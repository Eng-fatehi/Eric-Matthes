""" Return(generate) a full name, neatly fromatted."""
def get_formatted_name(first, middle, last):            # get formatted name function used to return full name.
    full_name = f"{first} {middle} {last}"                
    return full_name.title()


""" 
musician= get_formatted_name("jimi", "hendrix")
print(musician)
 """

'''
# Three way to write the same code:
#full_name = (f"{first} {last}")  # f string with parenthesis.
#full_name = f"{first} {last}"    # f string without parenthesis.        
#full_name = first+" "+last       # normal string.
'''

""" Return full name, neatly formatted."""
def get_formatted_name(first_name, lats_name, middel_name=""): # an empty default value
    if middel_name: #True of Fault
        full_name = f"{first_name} {middel_name} {lats_name}"  #True
    else: 
        full_name = f"{first_name} {lats_name}" #Fault
    return full_name.title()

musician = get_formatted_name("ali", "ben", "abdo")
print(musician)

musician = get_formatted_name("ali", "abdo")
print(musician)
    
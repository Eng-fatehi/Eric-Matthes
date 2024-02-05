""" Return full name, neatly formatted name"""
#Making an Argument Optional (provide extra information)
def get_formatted_name(first_name, middle_name, last_name):
    full_name = f"\n{first_name} {middle_name} {last_name}"
    return full_name.title()
musician = get_formatted_name("ali", "omer", "aref")
print(musician)
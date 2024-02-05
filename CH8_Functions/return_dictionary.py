""" Return dicitonary of information about a person."""
def build_person(first_name, last_name):
    person = {"first": first_name, "last": last_name} # Dictionary
    print(type(person))
    return person                  #The title cannot be used with a dictionary
    
musician = build_person("jimi", "hendrix") 
print(musician) 

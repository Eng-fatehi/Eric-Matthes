""" Refactoring: Example 2 """

from pathlib import Path
import json


def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """Greet the user by name."""
    path = Path('CH10_Files_and_Exceptions\Storing_data\ username.json')                   # CH10_Files_and_Exceptions\Storing_data\remember_me.py
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

greet_user()





""" 

username = "John"

if username:
    print("Username is not empty or None")
else:
    print("Username is empty or None")
    
     
If username has a value (in this case, "John"), the if statement evaluates to True, 
and it will print "Username is not empty or None". 
If username were an empty string ("") or None, the if statement would evaluate to False, 
and it would print "Username is empty or None".  
       
        
"""



""" 

def greet_user():
    print("Hello!")

# Call the function
greet_user()


In this example, greet_user() is a function that simply prints "Hello!". 
When you call greet_user(), it executes the code inside the function, 
resulting in "Hello!" being printed to the console.

"""


""" Refactoring: Example 1"""

from pathlib import Path 
import json

def greet_user():
    """ Greet the user by name. """
    path = Path('CH10_Files_and_Exceptions\Storing_data\ username.json')

    if path.exists():
        contents =path.read_text()
        username =json.loads(contents)
        print(f"Welcome back,{username}!")

    else:
        username = input("What is your name?")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {username}!")

greet_user()



""" 

def greet_user():
    print("Hello!")

# Call the function
greet_user()


In this example, greet_user() is a function that simply prints "Hello!". 
When you call greet_user(), it executes the code inside the function, 
resulting in "Hello!" being printed to the console.

"""


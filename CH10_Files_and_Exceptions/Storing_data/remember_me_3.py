from pathlib import Path
import json

path = Path('CH10_Files_and_Exceptions\Storing_data\ username.json') 

if path.exists():  # if 'username.json'exists, we load the username and print a personalized greeting to hte user. 
    contents = path.read_text()
    username = json.loads(contents)
    print(f"\nWelcome back, {username}!")

else: 
    username = input("What is your name? ")  
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {username}!")




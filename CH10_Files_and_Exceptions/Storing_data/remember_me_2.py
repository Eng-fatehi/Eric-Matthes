from pathlib import Path
import json


path = Path('CH10_Files_and_Exceptions\Storing_data\\username.json')    
contents = path.read_text()
username = json.loads(contents)

print(f"\nWelcome back, {username}!")



""" 
username = input("What is your name? ")
path = Path('CH10_Files_and_Exceptions\Storing_data\ username.json')    
contents = json.dumps(username)
path.write_text(contents)
print(f"We'll remember you when you come back, {username}!")
 """




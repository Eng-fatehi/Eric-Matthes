''' Using json.dumps() and json.loads() '''

from pathlib import Path
import json

path = Path('CH10_Files_and_Exceptions\Storing_data\ numbers.json')
numbers = path.read_text()       # read_text() function reads the entire contents of the file.
contents = json.loads(numbers)   # json.loads() function converts a JSON string into a python object.

print(contents)

# python objects is a list or dictionary.


""" 
path = Path('CH10_Files_and_Exceptions\Storing_data\ numbers.json')
path.read_text()       # read_text() function reads the entire contents of the file.
json.loads(path.read_text())   # json.loads() function converts a JSON string into a python object.

print(json.loads(path.read_text()))
 """
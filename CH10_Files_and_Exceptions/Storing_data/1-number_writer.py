''' Using json.dumps() and json.loads() '''

from pathlib import Path
import json                     # import the json module to work with JSON data in python.


numbers = [2, 3, 5, 7, 11, 13]   # pthon objects is a list or dictionary.

path = Path('CH10_Files_and_Exceptions\Storing_data\ numbers.json') # the path where the file 'numbers.json' will be stored.
contents = json.dumps(numbers)   # json.dumps() is used to generate a string from a python object 'numbers.
path.write_text(contents)        # write_text() method is used to write the generated string 'contents to a specific file 'numbers.json'on the specified path.



""" 
json.dumps([2, 3, 5, 7, 11, 13])   
Path('CH10_Files_and_Exceptions\Storing_data\ numbers.json').write_text(json.dumps([2, 3, 5, 7, 11, 13]) )       
"""


""" 
path = Path('K:\Py Code\Eric Matthes\CH10_Files_and_Exceptions\Writing_to_a_file\programming.txt')
path.write_text("I love programming.")

"""

from pathlib import Path
import json

# Read data as a string and convert it to a Python object.
path = Path('C:\CH/eq_data/month.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents) # json.loads() fucntion is used to covert the string into a python object.

# Create a more readable version of the data file.
path = Path('C:\CH/eq_data/readable_eq_data_month.geojson') # 
readable_contents = json.dumps(all_eq_data, indent=4) # json.dumps() function can take an optional indent argument.
path.write_text(readable_contents) # path.write_text() function is used to write the contents of the string to a file.



''' 
The indent=4 argument tells json.dumps() to use an indentation of 4 spaces. 
This makes the JSON output more human-readable by organizing the data
in a structured and visually appealing way.
'''

''' 
In Windows, the backslash \ is the standard directory separator used in file paths. 
Programming and scripting languages: 
Some programming languages, like Python and many others, 
accept forward slashes / as directory separators in file paths even on Windows systems. 
This is often helpful for writing cross-platform code that can work on both 
Windows and Unix-based systems without needing to change the directory separators.
'''


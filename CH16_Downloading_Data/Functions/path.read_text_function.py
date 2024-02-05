'''
The path.read_text() function in Python is used to read the contents of a file
and return them as a string. It's part of the pathlib module 
'''

from pathlib import Path

# Define the path to the file
file_path = Path('C:\CH/sitka_weather_07-2021_simple.csv') 

# Read the contents of the file as text
file_contents = file_path.read_text()#.splitlines()

# Print the contents of the file
print(file_contents)

'''
Explanation:

-from pathlib import Path
Imports the Path class from the pathlib module.

-file_path = Path('C:\CH/sitka_weather_07-2021_simple.csv')
Creates a Path object representing the file path. 


-file_contents = file_path.read_text()
Reads the contents of the file specified by file_path and 
stores it as a string in the file_contents variable.

-print(file_contents): 
Prints the contents of the file to the console.

'''
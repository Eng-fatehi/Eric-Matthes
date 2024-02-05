from pathlib import Path


contents = "I love programming.\n"  # \n is for new line.
contents += "I love creating new games.\n" # += is the same as append.
contents += "I also love working with data.\n"  # += is concatenation with the previous string. 

path = Path('K:\Py Code\Eric Matthes\CH10_Files_and_Exceptions\Writing_to_a_file\programming.txt')
path.write_text(contents)  # write_text() method is used to write to a specific file on the path.

'''
This program has no terminal output, 
but if you open the file (programming.txt) you will see the three newlines:
................................
I love programming.
I love creating new games.
I also love working with data.
................................

'''
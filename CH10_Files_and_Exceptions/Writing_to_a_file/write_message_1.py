from pathlib import Path


path = Path('K:\Py Code\Eric Matthes\CH10_Files_and_Exceptions\Writing_to_a_file\programming.txt')
path.write_text("I love programming.")




'''
This program has no terminal output, 
but if you open the file (programming.txt) you will see the three newlines:
................................
I love programming.
................................

'''
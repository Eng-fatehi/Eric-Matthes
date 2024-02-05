from pathlib import Path 
# import the Path object form the pathlib module.

path = Path ('K:\Py Code\Eric Matthes\CH10_Files_and_Exceptions\Reading_from_a_file\pi_digits.txt') 
# Path() is used to create a Path object ponts to the file (you can check that the file exists before working whti it).
# we build a Path object representing the file pi_digits.txt, which we assigned to the variable path.

contents = path.read_text()  
# read_text() is used to read the entire contents of the file.
# The contents of the file are are returned as a single string, which we assigned to (stored in) the variable contents.

contents = contents.rstrip()
# rstrip() is used to remove any whitespace characters from the right side of the string.
# We can strip تجريد  the trailing newline السطر الجديد الزائد character immediately after calling read_text()
# contents = path.read_text().rstrip()

print(contents)
# When we print the contents of the file, we see the entire contents of the text file.   



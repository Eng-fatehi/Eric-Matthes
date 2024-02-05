''' Working with a File's Contents. '''
from pathlib import Path 

path = Path ('K:\Py Code\Eric Matthes\CH10_Files_and_Exceptions\Reading_from_a_file\pi_digits.txt') 
# You can use an absolute path if a relative path doesn't work.

contents = path.read_text()  

lines = contents.splitlines()
# splitlines() method returns a list of all lines in the file by using the newline character as a separator, 
# and assign this list to (sotred in) the variable lines.

pi_string = '' # empty string used for concatenating strings together لربط السلاسل معا.
for line in lines:
    pi_string += line # concatenating strings with using +=
print(pi_string)
print(len(pi_string))

pi_string = ''
for line in lines:
    pi_string += line.lstrip()   # lstrip() method used to remove spaces from the left side of the string.
print(pi_string)
print(len(pi_string))







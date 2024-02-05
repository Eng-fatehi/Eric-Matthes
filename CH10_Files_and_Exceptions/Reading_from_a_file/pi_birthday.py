from pathlib import Path


path = Path('K:\Py Code\Eric Matthes\CH10_Files_and_Exceptions\Reading_from_a_file\pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

birthday = input("Enter your birthday, in the form mmddyy: ") # input() function is used to get user input.
if birthday in pi_string: # if statement is used to check if the birthday is in the first million digits of pi.
    print("Your birthday appears in the first million digits of pi!")
else: # else statement is used if the birthday is not in the first million digits of pi.
    print("Your birthday does not appear in the first million digits of pi.")

   
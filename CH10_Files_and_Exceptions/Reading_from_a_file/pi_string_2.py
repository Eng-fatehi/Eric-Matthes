from pathlib import Path


path = Path('K:\Py Code\Eric Matthes\CH10_Files_and_Exceptions\Reading_from_a_file\pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")  # print only the first 52 characters of the string 
print(len(pi_string))


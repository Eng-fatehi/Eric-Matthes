from pathlib import Path 

path = Path ('K:\Py Code\Eric Matthes\CH10_Files_and_Exceptions\Reading_from_a_file\pi_digits.txt') 
# You can use an absolute path if a relative path doesn't work.

contents = path.read_text()  

lines = contents.splitlines()
# splitlines() method returns a list of all lines in the file by using the newline character as a separator, 
# and assign this list to (sotred in) the variable lines.

for line in lines:  
    print(line)
# We then loop over htese lines and print each one of them one by one by using the for loop.

 



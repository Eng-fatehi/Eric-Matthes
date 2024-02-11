from pathlib import Path

path = Path('CH10_Files_and_Exceptions\Exceptions\Alice.txt')

try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"\nSorry, the file {path} does not exist.")  
else: 
    # Count the approximate number of words in the file:
    words = contents.split()
    num_words = len(words)
    print(f"\nThe file {path} has about {num_words} words.")

""" 
In these example, the code " contents = path.read_text(encoding='utf-8') " in the try block 
produces a FileNotFondError, 
so we write an excpet block that matches that error " FileNotFoundError " and than tell python
to print a friendly error messages.
 """
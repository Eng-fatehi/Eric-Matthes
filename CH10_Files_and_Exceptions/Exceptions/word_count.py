from pathlib import Path


def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        #print(f"\nSorry, the file {path} does noet exist.")
        pass    # do nothing if the file doesn't exist " I 'll want the program to fail silently when an exception occurs"
    else:
        # Count the approximate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"\nThe file {path} has about {num_words} words.")

filenames = ['CH10_Files_and_Exceptions\Exceptions\Alice.txt', 
             'CH10_Files_and_Exceptions\Exceptions\siddhartha.txt', 
             'CH10_Files_and_Exceptions\Exceptions\moby_dick.txt',
             'CH10_Files_and_Exceptions\Exceptions\little_women.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)
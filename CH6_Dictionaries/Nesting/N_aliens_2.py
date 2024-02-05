''' Create a Fleet of 30 Aliens.'''
# Nesting is store data in a list of dictionaries.


# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):   # 
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)


# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")                 # three dots is used to indicate more content following the loop.


# Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))  # str() function is used to convert the interger into a string.
print(f"Total number of aliens: {len(aliens)}")       # f_string is used to print the value of the variable.












'''
In Python, a "string" is a sequence of characters. 
It is a data type that represents textual data. 
Strings are used to store and manipulate text, such as words, sentences, 
or any sequence of characters. In Python, 
strings are enclosed in either single quotes (') or double quotes (").
'''

'''
Example 1: 

Converting an integer to a string

number = 42
string_number = str(number)

print("Original number:", number)
print("String representation:", string_number)

.....................
output:
Original number: 42
String representation: 42

'''



''' 
rang() function is used to generate a sequence of numbers.


# Example 1: range(stop)

for i in range(5):
    print(i)

# Output: 0, 1, 2, 3, 4



# Example 2: range(start, stop)

for i in range(2, 8):
    print(i)

# Output: 2, 3, 4, 5, 6, 7



# Example 3: range(start, stop, step)

for i in range(1, 10, 2):
    print(i)

# Output: 1, 3, 5, 7, 9

'''
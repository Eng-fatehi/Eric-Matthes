''' Looping Through All Key-Value Pairs.'''

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items(): # items() method is used for dictionaries to returns a sequence of key-value pairs.
    print(f"\nKey: {key}")
    print(f"Value: {value}")

""" 
items_list = list(user_0.items())
print(items_list)
 """
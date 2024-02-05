""" Looping Through a Dictionary's Keys in a Particular Order(في ترتيب خاص)."""
# We use a dictionary to sotre one kind of information abut many objects.
favorite_languages = {
    'jen': 'python',        # indent four spaces 
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
    }

""" 
language = favorite_languages['sarah'].title()
print(f"\nSarah's favorite language is {language}.")

language = favorite_languages['jen'].title()
print(f"Jen's favorite language is {language}.")

 """

""" 
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
 """

""" 
for name in favorite_languages.keys():  # keys() method used to returns all the keys in the dictionary. 
    print(name.title())
 """

for name in sorted(favorite_languages.keys()): 
    print(f"{name.title()}, thank you for taking the poll.")   

# sorted() method tells Python to get all the keys in dictionary and sort them before starting the loop.
# taking the poll اخذ الاستطلاع

""" 
# looping through all key-value pairs.
for key, value in favorite_languages.items(): # items() method returns a sequence of key-value pairs.
    print(f"\nKey: {key}")
    print(f"Value: {value}")
 """
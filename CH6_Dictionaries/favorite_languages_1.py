""" A Dictionary of Similar Objects """
# We use a dictionary to sotre one kind of information abut many objects.
favorite_languages = {
    'jen': 'python',        # indent four spaces 
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
    }


language = favorite_languages['sarah'].title()
print(f"\nSarah's favorite language is {language}.")

language = favorite_languages['jen'].title()
print(f"Jen's favorite language is {language}.")


""" 
# looping through all key-value pairs.
for key, value in favorite_languages.items(): # items() method returns a sequence of key-value pairs.
    print(f"\nKey: {key}")
    print(f"Value: {value}")
 """
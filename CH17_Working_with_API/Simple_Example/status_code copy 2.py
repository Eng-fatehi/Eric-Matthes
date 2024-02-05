import requests
import json

response = requests.get("https://api.github.com/search/repositories?q=language:python+sort:stars")

def jprint(obj):                              # function to pretty print JSON
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)  # sort_keys is used to sort the json keys.
    print(text)

jprint(response.json()) # jprint() function is used to pretty print json.


''' 
The dumps() function is particularly useful as we can use it to print 
a formatted string which makes it easier to understand the JSON output
'''


'''
The json library has two main functions:

json.dumps() — Takes in a Python object, and converts (dumps) it to a string.
json.loads() — Takes a JSON string, and converts (loads) it to a Python object.

'''



# https://www.dataquest.io/blog/python-api-tutorial/


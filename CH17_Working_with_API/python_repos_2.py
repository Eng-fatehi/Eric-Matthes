import requests   # requests is a third-party module that makes HTTP (Hypertext نص تشعبيTransfer Protocol) requests.


# Make an API call and storethe response.
url = "https://api.github.com/search/repositories"  # The main part of the URL 
url +="?q=language:python+sort:stars+stars:>10000"  #  الاستعلام الاستفسارThe query part of the URL

headers = {"Accept": "application/vnd.github.v3+json"} # the headers for the API call in dictonary by key and value.

r = requests.get(url, headers=headers) # r is a response object 
print(f"status code: {r.status_code}")  #  if the requst is successful, the status code will be 200.
print(r.status_code)

# Convert the response object to a dictionary.
response_dict = r.json() # use json() method on the response object to parse the response content as json.

# Process results.
#print(response_dict.keys())
print(response_dict['total_count'])

# Explore information about the repositories.
respostorie_dicts = response_dict['items']
print(len(respostorie_dicts))

# Examine the first repository.
respostorie_dict = respostorie_dicts[0]

print(len(respostorie_dict))

for key in sorted(respostorie_dict.keys()):
    print(key)










'''  https://api.github.com/search/repositories?q=language:python+sort:stars  '''

''' https://www.youtube.com/watch?v=9Kwnq4y7hzY&list=PLVCtnldBSr4-hJ6y3eLJqzdbP_wlagjAG&index=10 '''

''' https://www.youtube.com/watch?v=FW8NdB18AYM '''
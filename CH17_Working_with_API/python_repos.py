import requests

url = "https://api.github.com/search/repositories?q=language:python+sort:stars"

response = requests.get(url)
response_dictonary = response.json()
print(response_dictonary.keys())


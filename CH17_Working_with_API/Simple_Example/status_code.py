import requests

response = requests.get("https://api.github.com/search/repositories?q=language:python+sort:stars")
print(response.status_code)



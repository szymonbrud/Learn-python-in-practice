import requests

url = 'https://random-word-api.herokuapp.com/word?number=10'

res = requests.get(url)
content = res.json()

print(content)

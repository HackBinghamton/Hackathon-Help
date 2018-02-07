import requests

# Request information from URL
response = requests.get('https://api.reddit.com/user/daxaxelrod/about')
# Prints dictionary and attributes as string
print(response.text)
# Get API info in json() dict format
print(response.json())


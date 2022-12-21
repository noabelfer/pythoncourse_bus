import requests

BORED_URL = "https://www.boredapi.com/api/activity"
response = requests.get(BORED_URL)
print(response)

print(response.status_code)
print(response.text)
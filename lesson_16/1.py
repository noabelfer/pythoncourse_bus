import base64
import json

import requests

url_id = base64.urlsafe_b64encode("https://www.dalidatlv.co.il/".encode()).decode().strip("=")
# print(url_id)


import requests

url_base = "https://www.virustotal.com/api/v3/urls/"
url = url_base + url_id

headers = {"accept": "application/json",
            "x-apikey": open("/Users/noabelfer/Downloads/pythonfiles/keys/apikey.txt").read()
           }

# response_anal = requests.get(url, headers=headers)
# print(response_anal.text)
# print(type(response_anal))
# file_anal = json.loads(response_anal.text)
# print(f'reputation = {file_anal.get("data").get("attributes").get("reputation")}')
# print(response.text)

####scan


url = "https://www.virustotal.com/api/v3/urls"

payload = "url=https://www.dalidatlv.co.il/"
headers = {
    "accept": "application/json",
    "content-type": "application/x-www-form-urlencoded",
    "x-apikey": open("/Users/noabelfer/Downloads/pythonfiles/keys/apikey.txt").read()
}

response = requests.post(url, data=payload, headers=headers)
file = json.loads(response.text)
scan_id = file.get("data").get("id")
print(f'id: {scan_id}')
# print(response.text)
# print()
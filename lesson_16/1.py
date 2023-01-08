import base64
import json
import os
import requests

class VT(self):
################################################
    def analysis_url(url:str) ->str:
        url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")
        url_base = "https://www.virustotal.com/api/v3/urls/"
        url = url_base + url_id
        headers = {"accept": "application/json",
                    "x-apikey": os.environ["VT_API"]
                   }
        print(os.environ["VT_API"])
        response_anal = requests.get(url, headers=headers)
        file_anal = json.loads(response_anal.text)
        return(file_anal)
        return(f'reputation = {file_anal.get("data").get("attributes").get("reputation")}')

    # response_anal = requests.get(url, headers=headers)
    # print(response_anal.text)
    # print(type(response_anal))
    # file_anal = json.loads(response_anal.text)
    # print(f'reputation = {file_anal.get("data").get("attributes").get("reputation")}')
    # print(response.text)

    # def analysis_id(url_id:str) ->str:
    #
    #     url_base = "https://www.virustotal.com/api/v3/urls/"
    #     url = url_base + url_id
    #     headers = {"accept": "application/json",
    #                 "x-apikey": open("/Users/noabelfer/Downloads/pythonfiles/keys/apikey.txt").read()
    #                }
    #     response_anal = requests.get(url, headers=headers)
    #     file_anal = json.loads(response_anal.text)
    #     return(file_anal)
        #return(f'reputation = {file_anal.get("data").get("attributes").get("reputation")}')


    def scan(url) ->str:#id

        url_vt = "https://www.virustotal.com/api/v3/urls"

        payload = "url=" + url
        headers = {
            "accept": "application/json",
            "content-type": "application/x-www-form-urlencoded",
            "x-apikey": open("/Users/noabelfer/Downloads/pythonfiles/keys/apikey.txt").read()
        }

        response = requests.post(url_vt, data=payload, headers=headers)
        print(response)
        file = json.loads(response.text)
        scan_id = file.get("data").get("id")
        return(scan_id)
    # print(response.text)
    # print()

    # a = scan("https://cartasense-coldchain.com/")
    # #aHR0cHM6Ly9jYXJ0YXNlbnNlLWNvbGRjaGFpbi5jb20v
    # print(a)

    n = analysis_url("https://cartasense-coldchain.com/")
    print(n)

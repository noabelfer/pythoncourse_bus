import argparse
import base64
import json
import os
import requests
import sys
import pickle


class VT:
    def __init__(self, url: str, apikey):
        self.url = url
        self.apikey = apikey
        self.cache = {}

    def load_cache(self):
        try:
            with open('pickle.cache', 'rb') as f:
                print('load')
                self.cache = pickle.load(f)
                f.close()
        except FileNotFoundError:
            self.cache = {}

    def save_cache(self):
        print('save')
        with open('pickle.cache', 'wb') as f:
            pickle.dump(self.cache, f)
            f.close()

    def analysis_url(self) -> dict:
        self.load_cache()
        json_data = json.dumps(self.cache, indent=4, separators=(',', ': '))
        print('--------> ' + json_data)
        if (self.url in self.cache):
            return self.cache[self.url]
        # print(str(type(self.url)))

        url_id = base64.urlsafe_b64encode(self.url.encode()).decode().strip("=")
        url_base = "https://www.virustotal.com/api/v3/urls/"
        new_url = url_base + url_id
        headers = {"accept": "application/json",
                   "x-apikey": self.apikey
                   }
        # print(os.environ["VT_API"])
        response_anal = requests.get(new_url, headers=headers)
        file_anal = json.loads(response_anal.text)
        # return(f'reputation = {file_anal.get("data").get("attributes").get("reputation")}')
        data_url = ({'url': self.url,
                     'reputation': file_anal.get("data").get("attributes").get("reputation"),
                     'time': file_anal.get("data").get("attributes").get("last_analysis_date")})

        self.cache[self.url] = data_url
        self.save_cache()
        # json_data = json.dumps(data_url)
        # with open('data_url.json', "r") as file:
        #     data = json.load(file)
        # data[self.url]= data_url

        with open('data_url.json', 'w') as file:
            json.dump(self.cache, file)
        file.close()
        print(self.cache, 'ppp')
        return data_url

    def get_analize_from_file(self, url):
        with open("data_url.json") as f:
            data = json.load(f)
        if self.url not in data.keys():
            return print("not existing url")
        values = data[url]
        return values

    def scan(self) -> bool:
        url_vt = "https://www.virustotal.com/api/v3/urls"
        payload = "url=" + self.url
        headers = {
            "accept": "application/json",
            "content-type": "application/x-www-form-urlencoded",
            "x-apikey": self.apikey
        }

        response = requests.post(url_vt, data=payload, headers=headers)
        print(response)
        file = json.loads(response.text)
        scan_id = file.get("data").get("id")
        if response.status_code == 200:
            return True
    # print(response.text)
    # print()

    # a = scan("https://cartasense-coldchain.com/")
    # #aHR0cHM6Ly9jYXJ0YXNlbnNlLWNvbGRjaGFpbi5jb20v
    # print(a)

    # n = analysis_url("https://cartasense-coldchain.com/")
    # print(n)


if __name__ == '__main__':
    a = VT("https://edulabs.co.il/", "32cdd325e88f9126cf3fb455b301c3c17761e9b6c4c1fa4577255cedf069b74d")
    b = VT("https://postgresapp.com/", "32cdd325e88f9126cf3fb455b301c3c17761e9b6c4c1fa4577255cedf069b74d")
    #
    print(a.analysis_url())
    print(b.analysis_url())
    # print(a.get_analize_from_file("https://cartasense-coldchain.com"))
    a = VT("cartasense.com", "32cdd325e88f9126cf3fb455b301c3c17761e9b6c4c1fa4577255cedf069b74d")
    b = VT("ti.com", "32cdd325e88f9126cf3fb455b301c3c17761e9b6c4c1fa4577255cedf069b74d")
    print(a.analysis_url())
    print(b.analysis_url())


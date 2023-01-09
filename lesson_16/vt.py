import argparse
import base64
import concurrent
import json
import os
import pickle
import threading
from concurrent.futures import ThreadPoolExecutor
from datetime import timedelta, datetime, time
import time
import requests




class VT:
    def __init__(self, url: tuple, apikey):
        self.urls:tuple = url
        self.apikey = apikey
        self.cache = {}
        self.lock = threading.Lock()


    def load_cache(self):
        self.lock.acquire()
        try:
            with open('pickle.cache.pickle', 'rb') as f:
                print('load')
                self.cache = pickle.load(f)
                f.close()
                self.lock.release()
        except FileNotFoundError:
            self.cache = {}
            self.lock.release()


    def save_cache(self):
        print('save')
        self.lock.acquire()
        try:
            with open('pickle.cache.pickle', 'wb') as f:
                pickle.dump(self.cache, f)
                f.close()
        finally:
            self.lock.release()



    def analysis_url(self, url_indx:int) -> dict:
        url = self.urls[url_indx]
        self.load_cache()
        if (url in self.cache):
            timeepoch = self.cache[url]['time']
            time_analize = datetime.fromtimestamp(timeepoch)
            now = datetime.now()
            if now - timedelta(days=180) <= time_analize <= now:
                print('getting the info from cache')
                return(self.cache[url])

        url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")
        url_base = "https://www.virustotal.com/api/v3/urls/"
        new_url = url_base + url_id
        headers = {"accept": "application/json",
                    "x-apikey": self.apikey
                   }
        # print(os.environ["VT_API"])
        response_anal = requests.get(new_url, headers=headers)
        if response_anal.status_code !=200 or response_anal.text is None:
            if self.scan(url):
                return {}
            raise Exception('not existing url')

        file_anal = json.loads(response_anal.text)
        data_url = ({'url': url,
        'reputation':file_anal.get("data").get("attributes").get("reputation"),
        'time': file_anal.get("data").get("attributes").get("last_analysis_date")})


        self.cache[url]= data_url
        self.save_cache()
        print(data_url)



    def scan(self, url_str:int) ->bool:
        url = url_str
        url_vt = "https://www.virustotal.com/api/v3/urls"
        payload = "url=" + url
        headers = {
            "accept": "application/json",
            "content-type": "application/x-www-form-urlencoded",
            "x-apikey": self.apikey
        }

        response = requests.post(url_vt, data=payload, headers=headers)
        print(response)
        if response.status_code != 200:
            raise Exception ('scan failed')
        file = json.loads(response.text)
        scan_id = file.get("data").get("id")
        if response.status_code ==200:
            return True

    def run_as_threads(self):
        futures = []
        with ThreadPoolExecutor(max_workers=4) as executer:
            for i in range(len(self.urls)):
                futures.append(executer.submit(self.analysis_url,i))
            executer.shutdown()
        for f in concurrent.futures.as_completed(futures):
            print(f.result())

    # print(response.text)
    # print()

    # a = scan("https://cartasense-coldchain.com/")
    # #aHR0cHM6Ly9jYXJ0YXNlbnNlLWNvbGRjaGFpbi5jb20v
    # print(a)

    # n = analysis_url("https://cartasense-coldchain.com/")
    # print(n)

# if __name__ == '__main__':
#     try:
#          d = VT("bjkbjkbk","32cdd325e88f9126cf3fb455b301c3c17761e9b6c4c1fa4577255cedf069b74d")
#          print(d.analysis_url())
#          if d.analysis_url() == {}:
#              time.sleep(1)
#          print(d.analysis_url())
#
#     except Exception as e:
#         print (str(e))




    # a = VT("https://cartasense-coldchain.com/", "32cdd325e88f9126cf3fb455b301c3c17761e9b6c4c1fa4577255cedf069b74d" )
    # a.analysis_url()
    #
    # a.load_cache()
    # a.save_cache()
    # a.get_analize_from_file()


    # b = VT("https://postgresapp.com/", "32cdd325e88f9126cf3fb455b301c3c17761e9b6c4c1fa4577255cedf069b74d")
    # b.analysis_url()
    # b.load_cache()
    # b.save_cache()
    # b.get_analize_from_file()
    # print(a.analysis_url())
    #print(b.analysis_url())
    #print(a.get_analize_from_file("https://cartasense-coldchain.com"))
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
                print('loading information from cache')
                self.cache = pickle.load(f)
                f.close()
                self.lock.release()
        except FileNotFoundError:
            self.cache = {}
            self.lock.release()


    def save_cache(self):
        print('saving to cache')
        self.lock.acquire()
        try:
            with open('pickle.cache.pickle', 'wb') as f:
                pickle.dump(self.cache, f)
                f.close()
        finally:
            self.lock.release()


    def analysis_url(self, url:str) -> bool:
        while True:
            self.load_cache()
            if (url in self.cache):
                timeepoch = self.cache[url]['time']
                time_analize = datetime.fromtimestamp(timeepoch)
                now = datetime.now()

                if now - timedelta(days=180) <= time_analize <= now:
                    print('getting the info from cache')
                    return self.cache[url]


            url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")
            url_base = "https://www.virustotal.com/api/v3/urls/"
            new_url = url_base + url_id
            headers = {"accept": "application/json",
                        "x-apikey": self.apikey
                       }
            response_anal = requests.get(new_url, headers=headers)
            if response_anal.status_code !=200 or response_anal.text is None:
                if self.scan(url):
                    print('url has been scanned')
                    time.sleep(3)
                    continue
                raise Exception('not existing url')

            file_anal = json.loads(response_anal.text)
            time_e = file_anal.get("data").get("attributes").get("last_analysis_date")
            time_updated = datetime.fromtimestamp(time_e)

            data_url = ({'url': url,
                         'reputation': file_anal.get("data").get("attributes").get("reputation"),
                         'time': file_anal.get("data").get("attributes").get("last_analysis_date"),
                         'time_analyze':str(time_updated)})


            self.cache[url]= data_url
            self.save_cache()
            print(data_url)
            return False


    #scans the url for an updated analize
    def scan(self, url:str) ->bool:
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
            Error=str(response.status_code)
            raise Exception (f'scan failed, {url} got response {Error}')
        file = json.loads(response.text)
        scan_id = file.get("data").get("id")
        if response.status_code ==200:
            return True

    def run_as_threads(self):
        futures = []
        with ThreadPoolExecutor(max_workers=4) as executer:
            for u in self.urls:
                futures.append(executer.submit(self.analysis_url,u))
            executer.shutdown()
        for f in concurrent.futures.as_completed(futures):
            print(f.result())

    def scan_as_threads(self):
        futures = []
        with ThreadPoolExecutor(max_workers=4) as executer:
            for u in self.urls:
                futures.append(executer.submit(self.scan,u))
            executer.shutdown()
        for f in concurrent.futures.as_completed(futures):
            print(f.result())


import argparse
import base64
import json
import os
import pickle
from datetime import timedelta, datetime, time
import time
import requests

class VT:
    def __init__(self, url:str, apikey):
        self.url = url
        self.apikey = apikey
        self.cache = {}

    def load_cache(self):
        try:
            with open('pickle.cache.pickle', 'rb') as f:
                print('load')
                self.cache = pickle.load(f)
                f.close()
        except FileNotFoundError:
            self.cache = {}

    def save_cache(self):
        print('save')
        with open('pickle.cache.pickle', 'wb') as f:
            pickle.dump(self.cache, f)
            f.close()


    def analysis_url(self) -> dict:

        self.load_cache()
        if (self.url in self.cache):
            timeepoch = self.cache[self.url]['time']
            time_analize = datetime.fromtimestamp(timeepoch)
            now = datetime.now()
            if now - timedelta(days=180) <= time_analize <= now:
                print('getting the info from cache')
                return(self.cache[self.url])

        url_id = base64.urlsafe_b64encode(self.url.encode()).decode().strip("=")
        url_base = "https://www.virustotal.com/api/v3/urls/"
        new_url = url_base + url_id
        headers = {"accept": "application/json",
                    "x-apikey": self.apikey
                   }
        # print(os.environ["VT_API"])
        response_anal = requests.get(new_url, headers=headers)
        if response_anal.status_code !=200 or response_anal.text is None:
            if self.scan():
                return {}
            raise Exception('not existing url')

        file_anal = json.loads(response_anal.text)
        data_url = ({'url': self.url,
        'reputation':file_anal.get("data").get("attributes").get("reputation"),
        'time': file_anal.get("data").get("attributes").get("last_analysis_date")})


        self.cache[self.url]= data_url
        self.save_cache()
        print(data_url)



    def scan(self) ->bool:
        url_vt = "https://www.virustotal.com/api/v3/urls"
        payload = "url=" + self.url
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
    # print(response.text)
    # print()

    # a = scan("https://cartasense-coldchain.com/")
    # #aHR0cHM6Ly9jYXJ0YXNlbnNlLWNvbGRjaGFpbi5jb20v
    # print(a)

    # n = analysis_url("https://cartasense-coldchain.com/")
    # print(n)

if __name__ == '__main__':
    try:
         d = VT("bjkbjkbk","32cdd325e88f9126cf3fb455b301c3c17761e9b6c4c1fa4577255cedf069b74d")
         print(d.analysis_url())
         if d.analysis_url() == {}:
             time.sleep(1)
         print(d.analysis_url())

    except Exception as e:
        print (str(e))



#
#     parser = argparse.ArgumentParser(
#         prog='virustotal scanner',
#         description = 'bla bla',
#         epilog = 'fefefwes')
#
#     parser.add_argument('urls', nargs='+', help='List of urls to be scanned')
#     parser.add_argument('-s', '--scan', action='store_true', help='Scan')
#     parser.add_argument('--apikey', help='VTAPI user api key')
#
#     args = parser.parse_args()
#     print(args.urls, args.apikey, args.scan)
# #
#     urls = args.urls
#     toscan = args.scan
#     apikey = args.apikey
#
# if (apikey == None):
#     apikey = "32cdd325e88f9126cf3fb455b301c3c17761e9b6c4c1fa4577255cedf069b74d"
#
#

    # print('urls: '+str(urls)+' toscan: '+str(toscan) + ' apikey: '+str(apikey))
    #a = VT(urls[0],apikey)
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
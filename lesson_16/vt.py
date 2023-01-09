import argparse
import base64
import json
import os
import requests
import sys

class VT:
    def __init__(self, url:str, apikey):
        self.url = url
        self.apikey = apikey

    def analysis_url(self) ->str:
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
        return(f'reputation = {file_anal.get("data").get("attributes").get("reputation")}')



    def scan(self) ->str:#id
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
        return(scan_id)
    # print(response.text)
    # print()

    # a = scan("https://cartasense-coldchain.com/")
    # #aHR0cHM6Ly9jYXJ0YXNlbnNlLWNvbGRjaGFpbi5jb20v
    # print(a)

    # n = analysis_url("https://cartasense-coldchain.com/")
    # print(n)

if __name__ == '__main__':

    # d = VT("https://cartasense-coldchain.com/","32cdd325e88f9126cf3fb455b301c3c17761e9b6c4c1fa4577255cedf069b74d")
    # print(analysis_url())

    parser = argparse.ArgumentParser(
        prog='virustotal scanner',
        description = 'bla bla',
        epilog = 'fefefwes')

    parser.add_argument('urls', nargs='+', help='List of urls to be scanned')
    parser.add_argument('-s', '--scan', action='store_true', help='Scan')
    parser.add_argument('--apikey', help='VTAPI user api key')

    args = parser.parse_args()
    print(args.urls, args.apikey, args.scan)
#
    urls = args.urls
    toscan = args.scan
    apikey = args.apikey
#
# if (apikey == None):
#     apikey = "32cdd325e88f9126cf3fb455b301c3c17761e9b6c4c1fa4577255cedf069b74d"
#
#

    print('urls: '+str(urls)+' toscan: '+str(toscan) + ' apikey: '+str(apikey))
    a = VT(urls[0],apikey)
    print(a.analysis_url())
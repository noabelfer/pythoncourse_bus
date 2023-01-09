#!/usr/bin/env python
import argparse
import vtapi
import json
from lesson_16 import *

default_api_key = '32cdd325e88f9126cf3fb455b301c3c17761e9b6c4c1fa4577255cedf069b74d'

parser = argparse.ArgumentParser()

parser.add_argument('urls', nargs='+', help='List of urls to be scanned')
parser.add_argument('-s', '--scan', action='store_true', help='Scan')
parser.add_argument('--apikey', help='VTAPI user api key')

args = parser.parse_args()
print(args)

urls = args.urls
toscan = args.scan
apikey = args.apikey

if (apikey == None):
    apikey = default_api_key

print('urls: '+str(urls)+' toscan: '+str(toscan) + ' apikey: '+str(apikey))
# vt = vtapi.Vtapi(urls, apikey, toscan)
# vt.run_as_threads()
a = VT()
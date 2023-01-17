#! /usr/local/bin/python3.11
import argparse
import vt

parser = argparse.ArgumentParser(
    prog='main.py',
    description = 'scanning url using VT api',
    epilog = 'noa')

parser.add_argument('urls', nargs='+', help='List of urls to be scanned')
parser.add_argument('-s', '--scan', action='store_true', help='Scan')
parser.add_argument('-k', '--apikey', help='VTAPI user api key')

args = parser.parse_args()
print(args.urls, args.apikey, args.scan)
#
urls = args.urls
toscan = args.scan
apikey = args.apikey



print('urls: '+str(urls)+' toscan: '+str(toscan))
try:
    a = vt.VT(urls,apikey)
    if toscan:
        a.scan_as_threads()
    else:
        a.run_as_threads()
except Exception as e:
    print(str(e))

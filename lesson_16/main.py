#! /usr/local/bin/python3.11
import argparse
import vt

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

if (apikey == None):
    apikey = "32cdd325e88f9126cf3fb455b301c3c17761e9b6c4c1fa4577255cedf069b74d"


print('urls: '+str(urls)+' toscan: '+str(toscan) + ' apikey: '+str(apikey))
a = vt.VT(urls,apikey)

a.run_as_threads()

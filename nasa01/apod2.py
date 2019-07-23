#!/url/bin/env python3

import urllib.request
import json
import webbrowser
from pprint import pprint as pp

NASAAPI = 'https://api.nasa.gov/planetary/apod?'
MYKEY = 'api_key=hxyDl0yMKKL0i0597ScjAAk1scnvXZzH6SafaziE'

def main():
    """run-time code"""
    nasaapiobj = urllib.request.urlopen(NASAAPI + MYKEY)
    nasaread = nasaapiobj.read()
    convertedjson = json.loads(nasaread.decode('utf-8'))
    print(convertedjson)
    input('\nThis is converted JSON. Press Enter to continue.')

    pp(convertedjson)
    input('\nThis is pretty printed JSON. Press Enter to continue.')

    print(convertedjson['explanation'])
    input('\nPress Enter to view the photo of the day')

    webbrowser.open(convertedjson['hdurl'])
main()

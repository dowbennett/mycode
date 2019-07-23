#!/url/bin/env python3

import urllib.request
import json

neourl = 'https://api.nasa.gov/neo/rest/v1/feed?'
startdate = 'start_date=2018-06-01'
enddate = '&end_date=2019-07-23'
mykey = '&api_key=hxyDl0yMKKL0i0597ScjAAk1scnvXZzH6SafaziE'

neourl = neourl + startdate + mykey

neourlobj = urllib.request.urlopen(neourl)

neoread = neourlobj.read()

decodeneo = json.loads(neoread.decode('utf-8'))

print("\n\nConverted python data")
print(decodeneo)

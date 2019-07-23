#!/usr/bin/env python3

import requests

def main():
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?'
    startdate = 'start_date=2019-07-22'
    enddate = '&end_date=2019-07-23'
    mykey = '&api_key=hxyDl0yMKKL0i0597ScjAAk1scnvXZzH6SafaziE'

    neourl = neourl + startdate + mykey

    neojson = (requests.get(neourl)).json()

    print(neojson)

main()

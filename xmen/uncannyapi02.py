#!/usr/bin/env python3
import argparse
import time
import requests
import hashlib

XAVIER = 'http://gateway.marvel.com/v1/public/characters'

def hashbuilder(timeywimey, pvkee, pubkee):
    return hashlib.md5((timeywimey+pvkee+pubkee).encode('utf-8')).hexdigest()

def marvelcharcall(stampystamp, hashyhash, pkeyz, lookmeup):
    r = requests.get(XAVIER+"?name="+lookmeup+"&ts="+stampystamp+"&apikey="+pkeyz+"&hash="+hashyhash)
    print(XAVIER+"?name="+lookmeup+"&ts="+stampystamp+"&apikey="+pkeyz+"&hash="+hashyhash)
    return r.json()

def main():
    with open(args.dev) as mccoy:
        beast = mccoy.read().rstrip('\n')

    with open(args.pub) as munroe:
        storm = munroe.read().rstrip('\n')

    nightcrawler = str(time.time()).rstrip('.')

    cerebro = hashbuilder(nightcrawler, beast, storm)

    uncannyxmen = marvelcharcall(nightcrawler, cerebro, storm, args.hero)

    print(uncannyxmen)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dev', help='Provide the /path/to/file.priv containing Marvel private developer key')
    parser.add_argument('--pub', help='Provide the /path/to/file.pub containing Marvel public developer key')
    parser.add_argument('--hero', help='Character to search for within the Marvel universe')
    
    args = parser.parse_args()
    main()

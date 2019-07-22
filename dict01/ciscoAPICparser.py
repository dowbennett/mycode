#!/usr/bin/env python3

import json

def main():
    with open("ciscoAPIC.json", "r") as jsonfile:
        fog = json.load(jsonfile)
        print("The number of instance: ", len(fog['imdata']))
        for instances in fog['imdata']:
            print("Firmware version running - ", instances.get('firmwareCtrlrRunning').get('attributes').get('version'))
main()

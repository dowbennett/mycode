#!/usr/bin/env python3

def main():
    #Read in our data list
    networklists= []
    with open('driverip.txt','r') as driverip:
        for sline in driverip:
            networklists.append(sline.rstrip("\n").split(' '))

    print(networklists)

    for driveandip in networklists:
        print('SSH to ' + driveandip[1] + ' using driver ' + driveandip[0])

main()

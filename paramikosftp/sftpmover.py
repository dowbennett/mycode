#!/usr/bin/env python3
import paramiko
import os

hostip = input("Ip to connect to: ")
user = input("Username: ")
dest = input("Destination of files to copy: ")
t = paramiko.Transport(hostip,22)
t.connect(username=user,password="alta3")

sftp = paramiko.SFTPClient.from_transport(t)

def movethemfiles():
    for x in os.listdir("/home/student/filestocopy/"):
        if not os.path.isdir("/home/student/filestocopy"+x):
            sftp.put("/home/student/filestocopy/"+x,dest+x)
movethemfiles()

sftp.close()

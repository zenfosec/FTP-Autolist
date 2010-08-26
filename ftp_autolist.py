#!/usr/bin/env python

from ftplib import FTP
import ftplib
import sys
import string
from collections import deque

host = sys.argv[1]
ftp = FTP(host)
ftp.connect()
print ftp.getwelcome()
ftp.login()

masterdirlist = deque(["/"])

while len(masterdirlist) > 0:
    dirtolist = masterdirlist.popleft()
    print dirtolist
    lines = []
    try:
        ftp.dir(dirtolist,lines.append)
    except: ftplib.all_errors
    try:
        ftp.dir(dirtolist)
    except: ftplib.all_errors
    for line in lines:
        if line.startswith("d") or "<DIR>" in line:
            tempdir=line.split()[-1]
            if dirtolist == "/":
                masterdirlist.append(dirtolist + tempdir)
            else:    
                masterdirlist.append(dirtolist + "/" + tempdir)        

ftp.quit()
from icmplib import ping
from time import time
import sys

from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

stan = None

if len(sys.argv)<2:
    print("You need to add IP as argument")

while True:
    w = ping(sys.argv[1], count=2, interval=1, timeout=2, id=None, source=None, family=None, privileged=False)
    if stan == w.is_alive:
        pass
    else:
        stan = w.is_alive
        if w.is_alive:
            print(f'Host {sys.argv[1]} is online: {dt_string}')
        else:
            print(f'Host {sys.argv[1]} is offline: {dt_string}')
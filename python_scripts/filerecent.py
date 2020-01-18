#!/usr/bin/env python
import os
import time
import sys

directory = sys.argv[1] ##path of the directory

try:
    t = int(sys.argv[2]) ## in seconds
except IndexError:
    t = 1

currtime = time.time(); t = t*3600

def calc_time(minutes):
    # create neatly displayed time
    if minutes < 60:
        return "-----edited "+str(minutes)+" minutes ago!!"
    else:
        hrs = int(minutes/60); minutes = int(minutes - hrs*60)
        return "----edited "+str(hrs)+" hours and "+str(minutes)+" minutes ago!!"

for root, dirs, files in os.walk(directory):
    for file in files:
        file = os.path.join(root, file); ftime = os.path.getctime(file)
        edited = currtime - ftime
        if edited < t:
            print(file, calc_time(int(edited/60)))

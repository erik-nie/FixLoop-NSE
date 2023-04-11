# CheckLoopPoints.py
# Check all folders recursively

import wavfile 
import glob
import os

from pathlib import Path

def checkLoopPoints( filename ):
    try:
        r = wavfile.read(filename,readloops=True)
        start = r[3][0][0]
        end = r[3][0][1]
        print(filename, start, end)
    except Exception as err:
        #print(f"{filename=} Unexpected {err=}, {type(err)=}")
        print(filename ," NO LOOP POINTS ")
                
def recurse_path(target_path, level=0):
    for file in target_path.iterdir():
        if file.is_dir():
            recurse_path(file, level+1)
        else:
            checkLoopPoints(file.resolve())

my_path = Path(r'.')
recurse_path(my_path)


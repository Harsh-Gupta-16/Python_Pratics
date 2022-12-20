import glob
import os

read_files=glob.glob('Tracker*.xls')
with open("result.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())

for delfile in read_files:
    os.remove(delfile)
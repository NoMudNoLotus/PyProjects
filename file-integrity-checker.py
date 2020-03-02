#!/usr/bin/env python
# file integrity checker by nomudnolotus
import os
import hashlib
import time

files={}
while True:
    # for each file in directory: add to list
    for file in [item for item in os.listdir('.') if os.path.isfile(item)]:
        hash = hashlib.md5()
        with open(file, encoding='utf-8') as f: # encode unicode string into bytes for md5
            for chunk in iter(lambda: f.read(2048), ""): # break file into chunks
                hash.update(chunk)
        md5 = hash.hexdigest()
        if (file in files and md5 != files[file]):
            print("{}\t{} has been changed!".format(time.strftime("%Y-%m-%d %H:%M:%S") , file))
        files[file]=md5
    time.sleep(1)

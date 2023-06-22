#!/usr/bin/env python3
# annot pt w/ chloe

import sys
import requests
import pandas as pd
from IPython.display import SVG

# parse input filename
file = sys.argv[1]
outname=file.rsplit(".",1)
outname=outname[0]
#outname=file.split(".")[0:-1]
#outname="".join(outname)

# open file
fd=open(file, "rb")

# run chloe
CHLOE = 'https://chloe.plastid.org'

res = requests.post(CHLOE + '/annotate', files=dict(file=fd)).json()

# process request
while 1 == 1:
    if 'task_url' in res:
        res = requests.get(CHLOE + res['task_url']).json()
        print(res['status'])
    if res['status'] == "SUCCESS":
        print("API request succeeded!")
        break
    elif res['status'] == "FAILURE":
        print("API request failed- exiting!")
        sys.exit() 

# dl output
gff = requests.get(CHLOE + res['download_gff']).text
image=SVG(requests.get(CHLOE + res['view_svg']).content)

# write out
with open(outname + ".gff", "w") as f:
    f.write(gff)

with open(outname + ".svg",'wb+') as outfile:
    outfile.write(image.data.encode('utf-8'))

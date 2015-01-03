__author__ = 'Dean'

import sys

line = 3000000

def pp(s):
    sys.stdout.write(s)

outfile = open("testdata.csv", "a+")

fn="john"
ln="doe"
em="@ibm.com"
site="www.ibm.com"

while(line>0):
    curFn = fn+str(line)
    curLn = ln+str(line)
    curEm = str(line)+em
    curSite = site
    outfile.write(curFn+","+curLn+","+curEm+","+curSite+"\n")
    line-=1

outfile.close()



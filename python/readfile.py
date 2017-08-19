#!/usr/local/bin/python
# Function to read a comma delimited file 
# by David R. Larsen, November 13, 2012
# Creative Commons,  http://creativecommons.org/licenses/by-nc/3.0/us/

import sys
from string import strip


def readfile( file ):
   count = 0
   while 1:
      line = file.readline()
      print line.rstrip('\n')
      if not line: break
      count = count + 1
   
if len(sys.argv) == 1:
  readfile(sys.stdin)
else:
  readfile(open(sys.argv[1], 'r' ))


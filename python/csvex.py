#!/usr/local/bin/python
# Function to read a comma delimited file 
# by David R. Larsen, November 13, 2012
# Creative Commons,  http://creativecommons.org/licenses/by-nc/3.0/us/

import csv, sys, string

def readcsv( file ):
  with file as csvfile:
     spamreader = csv.reader(csvfile)
     for row in spamreader:
       if( row[0].startswith( '#' ) ):
         print "Comment"
         print ','.join(row), '\n'
       else:
	 print ' '.join(row[0::1::4])
       
if len(sys.argv) == 1:
  readcsv(sys.stdin)
else:
  readcsv(open(sys.argv[1], 'r' ))
      
#!/usr/local/bin/python
# Function to calculate the stand density index 
# from trees per acre and quadratic Mean diameter
# by David R. Larsen, October 12, 2012
# Creative Commons,  http://creativecommons.org/licenses/by-nc/3.0/us/

import math

def sdi( tpa, qmd, unittype="imperial"):
    if( unittype == "imperial" ):
       value = tpa * ( qmd / 10.0 )**1.605	
       return value
    elif( unittype == "metric"):
       value = tpa * ( qmd / 25.4 )**1.605
       return value
    else:
       print "Unknown unittype, options are imperial or metric"
       return 

print "sdi =", sdi( 200.0, 12.3)
print "sdi =", sdi( 200.0, 12.3, "imperial")
print "sdi =", sdi( 494.1, 31, "metric")
print "sdi =", sdi(1, 1, "cuni:xts")
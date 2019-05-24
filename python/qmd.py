#!/usr/local/bin/python
# Function to calculate the quadratic mean diameter 
# from basal area and tree per acre
# by David R. Larsen, October 11, 2012
# Creative Commons,  http://creativecommons.org/licenses/by-nc/3.0/us/

import math

def qmd( ba, tpa, unittype="imperial"):
    if( unittype == "imperial" ):
       value = math.sqrt( (ba/tpa)/0.005454154 )	
       return value
    elif( unittype == "metric"):
       value = math.sqrt( (ba/tpa)/0.00007854 )
       return value
    else:
       print( "Unknown unittype, options are imperial or metric")
       return 

print( "qmd =", qmd(80.0, 200.0))
print( "qmd =", qmd(80.0, 200.0, "imperial"))
print( "qmd =", qmd(18.3, 494.1, "metric"))
print( "qmd =", qmd(1.0, 1.0, "cunits"))
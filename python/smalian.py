#!/usr/local/bin/python
# Function to calculate the frustum of a paraboloid 
# from small end diameter, large end diameter and log length
# by David R. Larsen, October 30, 2012
# Creative Commons,  http://creativecommons.org/licenses/by-nc/3.0/us/

import math

def smalian( sdia, ldia, length, unittype="imperial", sameunits=False):
    if( unittype == "imperial" ):
       if( sameunits == True ):
         As = math.pi * sdia**2.0
         Al = math.pi * ldia**2.0
       else:
	 As = math.pi * (sdia/12.0)**2.0
         Al = math.pi * (ldia/12.0)**2.0
         
       value = length / 2.0 * ( As + Al )	
       return value
    elif( unittype == "metric"):
       if( sameunits == True ):
         As = math.pi * sdia**2.0
         Al = math.pi * ldia**2.0
       else:
	 As = math.pi * (sdia/100.0)**2.0
         Al = math.pi * (ldia/100.0)**2.0
         
       value = length / 2.0 * ( As + Al )
       return value
    else:
       print( "Unknown unittype, options are imperial or metric"
       return 

print( "smalian =", smalian( 11.0, 10.0, 16.0))
print( "smalian =", smalian( 11.0, 10.0, 16.0, "imperial"))
print( "smalian =", smalian( 28.0, 25.0, 4.8, "metric"))
print( "smalian =", smalian(11.0, 10.0, 16.0, "cunits"))

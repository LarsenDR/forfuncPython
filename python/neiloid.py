#!/usr/local/bin/python
# Function to calculate the frustum of a neloid 
# from small end diameter, large end diameter and log length
# by David R. Larsen, October 30, 2012
# Creative Commons,  http://creativecommons.org/licenses/by-nc/3.0/us/

import math

def neloid( sdia, ldia, length, unittype="imperial", sameunits=False):
    if( unittype == "imperial" ):
       if( sameunits == True ):
         As = math.pi * sdia**2.0
         Al = math.pi * ldia**2.0
       else:
	 As = math.pi * (sdia/12.0)**2.0
         Al = math.pi * (ldia/12.0)**2.0
         
       value = length / 4.0 * ( As + ( As**2.0 * Al)**(1.0/3.0) + (As * Al**2.0)**(1.0/3.0) + Al )
       return value
    elif( unittype == "metric"):
       if( sameunits == True ):
         As = math.pi * sdia**2.0
         Al = math.pi * ldia**2.0
       else:
	 As = math.pi * (sdia/100.0)**2.0
         Al = math.pi * (ldia/100.0)**2.0
         
       value = length / 4.0 * ( As + ( As**2.0 * Al)**(1.0/3.0) + (As * Al**2.0)**(1.0/3.0) + Al )
       return value
    else:
       print( "Unknown unittype, options are imperial or metric"
       return 

print( "neloid =", neloid( 11.0, 10.0, 16.0))
print( "neloid =", neloid( 11.0, 10.0, 16.0, "imperial"))
print( "neloid =", neloid( 28.0, 25.0, 4.8, "metric"))
print( "neloid =", neloid(11.0, 10.0, 16.0, "cuni:xts"))
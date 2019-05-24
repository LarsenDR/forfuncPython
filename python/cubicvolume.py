#!/usr/local/bin/python
# Function to calculate  cubic volume 
# from small end diameter, large end diameter and log length
# by David R. Larsen, October 30, 2012
# Creative Commons,  http://creativecommons.org/licenses/by-nc/3.0/us/

import math

def cbrt( a ):
    cubert= (a**(1 / 3.0))
    return cubert
    
def cubicvolume( sdia, ldia, length, equationtype="smailian", unittype="imperial", sameunits=False):
    if( unittype == "imperial" ):
       if( sameunits == True ):
         As = math.pi * sdia**2.0
         Al = math.pi * ldia**2.0
       else:
         As = math.pi * (sdia/12.0)**2.0
         Al = math.pi * (ldia/12.0)**2.0
       
       if( equationtype == "smailian" ): 
          value = length / 2.0 * ( As + Al )	
          return value
       elif( equationtype == "cone"): 
          value = length / 3.0 * ( As + math.sqrt( As * Al) + Al )
          return value
       elif (equationtype == "neiloid" ):
          value = length / 4.0 * ( As + cbrt( As ** 2 * Al) + cbrt( As * Al ** 2) + Al )
          return value
    elif( unittype == "metric"):
       if( sameunits == True ):
         As = math.pi * sdia**2.0
         Al = math.pi * ldia**2.0
       else:
         As = math.pi * (sdia/100.0)**2.0
         Al = math.pi * (ldia/100.0)**2.0
       
       if( equationtype == "smailian" ):
          value = length / 2.0 * ( As + Al )
          return value
       elif( equationtype == "cone"): 
          value = length / 3.0 * ( As + math.sqrt( As * Al) + Al )
          return value
       elif (equationtype == "neiloid" ):
          value = length / 4.0 * ( As + cbrt( As ** 2 * Al) + cbrt( As * Al ** 2) + Al )
          return value
    else:
       print( "Unknown unittype, options are imperial or metric"
       return 

print( "smalian =", cubicvolume( 11.0, 10.0, 16.0))
print( "smalian =", cubicvolume( 11.0, 10.0, 16.0, "smailian", "imperial"))
print( "smalian =", cubicvolume( 28.0, 25.0, 4.8, "smailian", "metric"))
print( "smalian =", cubicvolume( 11.0, 10.0, 16.0, "smailian", "cunits"))
print( "cone =", cubicvolume( 11.0, 10.0, 16.0, "cone"))
print( "cone =", cubicvolume( 11.0, 10.0, 16.0, "cone", "imperial"))
print( "cone =", cubicvolume( 28.0, 25.0, 4.8, "cone", "metric"))
print( "cone =", cubicvolume( 11.0, 10.0, 16.0, "cone", "cunits"))
print( "neiloid =", cubicvolume( 11.0, 10.0, 16.0, "neiloid"))
print( "neiloid =", cubicvolume( 11.0, 10.0, 16.0, "neiloid", "imperial"))
print( "neiloid =", cubicvolume( 28.0, 25.0, 4.8, "neiloid", "metric"))
print( "neiloid =", cubicvolume( 11.0, 10.0, 16.0, "neiloid", "cunits"))

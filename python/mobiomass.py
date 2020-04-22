#!/usr/local/bin/python
# Function to calculate the quadratic mean diameter 
# from basal area and tree per acre
# by David R. Larsen, April 22, 2020
# Creative Commons,  http://creativecommons.org/licenses/by-nc/3.0/us/

import math

def mobiomass( dbh, mht, species="black"):
    if( species == "black" ):
       value = 1.67079 + 0.04796*math.pow(dbh, 2) + 0.81549*math.log(math.pow(dbh, 2)*mht)	
       return value
    elif( species == "post"):
       value = -0.50714 + 0.01655*math.pow(dbh, 2) + 0.81549*math.log(math.pow(dbh, 2)*mht)
       return value
    elif( species == "hickory"):
       value = 0.70177 + 0.05791*math.pow(dbh, 2) + 0.60755*math.log(math.pow(dbh, 2)*mht)
       return value
    elif( species == "white"):
       value = 0.61557 + 0.00373*math.pow(dbh, 2) + 0.71159*math.log(math.pow(dbh, 2)*mht)
       return value
    else:
       print( "Unknown unittype, options are black, post, hickory, white")
       return 

print("black oak, 14.3, 24.0, imperial", mobiomass(14.3, 24.0, "black"))
print("white oak, 22.6, 32.0, imperial", mobiomass(22.6, 32.0, "white"))
print("scarlet oak, 18.9, 18.0 imperial", mobiomass(18.9, 18.0, "hickory"))
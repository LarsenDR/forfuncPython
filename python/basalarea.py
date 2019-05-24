#!/usr/local/bin/python
# Function to calculate the basal area per acre 
# from diameter and weight
# by David R. Larsen, October 11, 2012
# Creative Commons,  http://creativecommons.org/licenses/by-nc/3.0/us/


def basalarea( dia=[], weight=[], unittype="imperial"):
    idx = 1
    value = 0
    for d in dia:
       if( unittype == "imperial" ):
          value = value + 0.005454154 * d**2 * weight[idx] 	         
       elif( unittype == "metric"):
          value = value + 0.00007854 * d**2 * weight[idx]
       else:
          print( "Unknown unittype, options are imperial or metric" )
          return
    idx = idx + 1      
    next
    return value

print( "basalarea =", basalarea(dia=[8,6,8,5,4,6,7],weight=[10,10,10,10,10,10,10] ))
print( "basalarea =", basalarea(dia=[8,6,8,5,4,6,7],weight=[10,10,10,10,10,10,10], unittype="imperial" ))
print( "basalarea =", basalarea(dia=[8,6,8,5,4,6,7],weight=[25,25,25,25,25,25,25], unittype="metric" ))
print( "basalarea =", basalarea([1], [1], "cunits"))

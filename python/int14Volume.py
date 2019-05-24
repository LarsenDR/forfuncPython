#!/usr/local/bin/python
# Function to calculate the International 1/4" Board foot volume 
# from small end diameter and log length
# by David R. Larsen, October 11, 2012
# Creative Commons,  http://creativecommons.org/licenses/by-nc/3.0/us/


def int14Volume( sdia, length):
    if( length == 4 ):
      value = 0.22 * sdia**2 - 0.71 * sdia
    elif( length == 8 ):
      value = 0.44 * sdia**2 - 1.20 * sdia - 0.30
    elif( length == 12 ):
      value = 0.66 * sdia**2 - 1.47 * sdia - 0.79
    elif( length == 16 ):
      value = 0.88 * sdia**2 - 1.52 * sdia - 1.36
    elif( length == 20 ):
      value = 1.10 * sdia**2 - 1.35 * sdia - 1.90
    elif( length == 24 ):
      value = 1.10 * sdia**2 - 1.35 * sdia - 1.90 + 0.22 * sdia**2 - 0.71 * sdia
    elif( length == 28 ):
      value = 1.10 * sdia**2 - 1.35 * sdia - 1.90 + 0.44 * sdia**2 - 1.20 * sdia - 0.30
    elif( length == 32 ):
      value = 1.10 * sdia**2 - 1.35 * sdia - 1.90 + 0.66 * sdia**2 - 1.47 * sdia - 0.79
    elif( length == 36 ):
      value = 1.10 * sdia**2 - 1.35 * sdia - 1.90 + 0.88 * sdia**2 - 1.52 * sdia - 1.36
    elif( length == 40 ):
      value = (1.10 * sdia**2 - 1.35 * sdia - 1.90) * 2 
    return value

print( "International 1/4 volume =", int14Volume(sdia=10,length=16))
print( "International 1/4 volume =", int14Volume(sdia=28,length=16))

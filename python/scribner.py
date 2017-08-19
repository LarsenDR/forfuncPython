#!/usr/local/bin/python
# Function to calculate the Scribner Board foot volume 
# from small end diameter and log length
# by David R. Larsen, October 11, 2012
# Creative Commons,  http://creativecommons.org/licenses/by-nc/3.0/us/


def scribner( sdia, length):
    value = ( 0.79 * sdia**2 - 2 * sdia - 4 ) * (length / 16)
    return value

print "scribner =", scribner(sdia=10,length=16)
print "scribner =", scribner(sdia=28,length=16)
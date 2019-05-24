#!/usr/local/bin/python
# Function to calculate the Doyle Board foot volume 
# from small end diameter and log length
# by David R. Larsen, October 11, 2012
# Creative Commons,  http://creativecommons.org/licenses/by-nc/3.0/us/


def doyle( sdia, length):
    value = (( sdia - 4.0) / 4.0 )**2 * length
    return value

print( "doyle =", doyle(sdia=10,length=16))
print( "doyle =", doyle(sdia=28,length=16))

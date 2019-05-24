#!/usr/local/bin/python
#
# Function to calculate percent stocking
# from basal area per acre and tree per acre
#
# by David R. Larsen, November 16, 2012
# Creative Commons,  http://creativecommons.org/licenses/by-nc/3.0/us/

import math

#
# Percent stocking has only been worked out for imperial measurements
#

def parameters(type="upland.oak"):
  if( type == "upland.oak" ):
     value = [-0.00507,0.01698,0.00307]
  elif( type == "northern.red.oak" ):
     value = [0.02476,0.006272,0.00469]
  else:
     value = [-0.00507,0.01698,0.00307]
  return value

#
# qmd is a function to return the quadratic mean diameter 
# given basal area per acre and trees per acre
#

def qmd( ba, tpa):
  value = math.sqrt( ((ba/tpa)/0.005454154) )	
  return value
#
# percentStocking is a function that return the percent stocking using a Gingrich style tree area equation
#
   
def percentStocking( ba, tpa, type="upland.oak" ):
  dia = qmd( ba, tpa )
  amd = -0.259 + 0.973 * dia
  b = parameters( type )
  percent = (b[0] + b[1] * amd + b[2] * dia**2 ) * tpa
  if( percent < 0.0 ):
    percent = 0.0
  return percent
  

# testing
print( "      percent stocking( 55, 100, \"upland.oak\") = ", percentStocking( 55.0, 100.0, type="upland.oak"))
print( "     percent stocking( 100, 200, \"upland.oak\") = ", percentStocking( 100.0, 200.0, type="upland.oak"))
print( "percent stocking( 50, 100, \"northern.red.oak\") = ", percentStocking( 50.0, 100.0, type="northern.red.oak"))
print( "      percent stocking( 100, 50, \"upland.oak\") = ", percentStocking( 100.0, 50.0, type="upland.oak"))
print( "      percent stocking( 50, 400, \"upland.oak\") = ", percentStocking( 50.0, 400.0, type="upland.oak"))

#!/usr/local/bin/python
# Function to calculate mean acorn weight (in lb) from dbh and species and trees per acre
# by David R. Larsen, Copyright October 9, 2012
# Creative Commons http://creativecommons.org/licenses/by-nc/3.0/us/

def acornwt(dbh, species):
  if( (species == "black") and (dbh > 9.9) and (dbh < 36.1) ):
    acornwt = -1.9065 + 0.2973 * dbh

  elif((species == "chestnut") and (dbh > 9.9) and (dbh < 36.1)):
    acornwt = 0.0008271 * dbh**3 - 0.08157 * dbh**2 + 2.692 * dbh - 18.85

  elif(species == "red" and dbh > 9.9 and dbh < 36.1):
    acornwt = 0.0004016 * dbh**4 - 0.0349937 * dbh**3 + 0.9864357 * dbh**2 - 9.5233885 * dbh + 27.32720516

  elif(species == "scarlet" and dbh > 9.9 and dbh < 36.1):
    acornwt = 0.0005975 * dbh**4 - 0.05325 * dbh**3 + 1.651 * dbh**2 - 19.97 * dbh + 84.71

  elif(species == "white" and dbh > 9.9 and dbh < 36.1):
    acornwt = 0.0001987 * dbh**4 - 0.02027 * dbh**3 + 0.694 * dbh**2 - 8.768 * dbh + 37.36

  else:
    acornwt = 0.0
 
  return acornwt  

	
<<<<<<< HEAD
print( "imperial =", acornwt( 14.3, "black" ))
print( "imperial =", acornwt( 22.6, "white" ))
print( "imperial =", acornwt( 18.9, "scarlet" ))
=======
print "black oak, 14.3, imperial =", acornwt( 14.3, "black" )
print "white oak, 22.6, imperial =", acornwt( 22.6, "white" )
print "scarlet oak, 18.9, imperial =", acornwt( 18.9, "scarlet" )
>>>>>>> ecf78d3b7d543d42dbb856c2ebf8602ae9ceb81c

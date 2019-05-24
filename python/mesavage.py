#!/usr/local/bin/python
# Function to calcaualte the Mesavage and Girard 1946 volume. 
# using the equations by H.V. Wiant, Jr., 1986, Formula's for
# Mesavage and Girard's Volume Tables, Northern Journal of Applied Forestry 3:124.
# Coded by David R. Larsen, June 20, 2015

# Creative Commons,  http://creativecommons.org/licenses/by-nc/3.0/us/


def mesavage( dbh, mht, volumeType="Doyle", girard=78.0):
    if ( mht > 0.0 ):
      L = mht / 16.0
      cor = (1.0+ ((girard - 78.0) * 0.03))

      if( volumeType == "Int1/4" ):
          a = [-13.35212, 9.58615, 1.52968]
          b = [1.79620, -2.59995, -0.27465]
          c = [0.04482, 0.45997, -0.00961]

      elif( volumeType == "Scribner" ):
          a = [-22.50365, 17.53508, -0.59242]
          b = [3.02888, -4.34381, -0.02302]
          c = [-0.01969, 0.51593, -0.02035]
    
      elif( volumeType == "Doyle" ):
          a = [-29.37337, 41.51275, 0.55743]
          b = [2.78043, -8.77272, -0.04516]
          c = [0.04177, 0.59042,  -0.01578]

      else:
	  volume = 0.0

    v1 = (a[0] + a[1] * L + a[2] * L**2) 
    v2 = (b[0] + b[1] * L + b[2] * L**2) * dbh 
    v3 = (c[0] + c[1] * L + c[2] * L**2) * dbh**2 
    volume = (v1 + v2 + v3) * cor
          
    return volume 

print( "Int 1/4 (78) =", mesavage(dbh=24.0,mht=40,volumeType="Int1/4", girard=78))
print( "Int 1/4 (82) =", mesavage(dbh=24.0,mht=40,volumeType="Int1/4", girard=82))
print( "Scribner (78) =", mesavage(dbh=24.0,mht=40,volumeType="Scribner", girard=78))
print( "Scribner (82) =", mesavage(dbh=24.0,mht=40,volumeType="Scribner", girard=82))
print( "Doyle (78) =", mesavage(dbh=24.0,mht=40,volumeType="Doyle", girard=78))
print( "Doyle (82) =", mesavage(dbh=24.0,mht=40,volumeType="Doyle", girard=82))

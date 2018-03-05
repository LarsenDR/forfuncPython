#!/usr/local/bin/python
# Function to calculate the Beers, 1964 tree volume 
# from diameter at breast height and merchantable height
# by David R. Larsen, October 11, 2012
# Creative Commons,  http://creativecommons.org/licenses/by-nc/3.0/us/


def treeVolume( dbh, mht, volumeType="boardfeet"):
    if ( mht > 0.0 ):
       a = (dbh**2 * (dbh + 190.0))/ 100000.0
       b = 1.0/100.0 * ((mht * (168.0 - mht))/64.0 + (32.0/mht))
       c = 475.0 + (3.0 * mht**2) / 128.0
       
       if( volumeType == "cords" ):
          volume = a * b
       elif( volumeType == "cubic" ):
          volume = 76.0 * a * b
       elif( volumeType == "cubicbark" ):
          volume = 92.0 * a * b
       elif( volumeType == "boardfeet" ):
          volume = a * b * c
       else:
	  volume = 0.0
          
    return volume 

print "Cords =", treeVolume(dbh=10,mht=26,volumeType="cords")
print "Cubic =", treeVolume(dbh=10,mht=26,volumeType="cubic")
print "Cubic with bark =", treeVolume(dbh=10,mht=26,volumeType="cubicbark")
print "International 1/4 boardfeet =", treeVolume(dbh=10,mht=26,volumeType="boardfeet")
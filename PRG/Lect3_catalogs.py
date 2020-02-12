import datetime
print('Hi! What\'s up? \nToday is ', datetime.datetime.now(), ' in UTC \n')

import numpy as np


#Haversine formula - angular distance
def angular_dist(ra1, dec1, ra2, dec2):
  ra1_r = np.radians(ra1)
  ra2_r = np.radians(ra2)
  dec1_r = np.radians(dec1)
  dec2_r = np.radians(dec2)
  a = np.sin(np.abs(dec1_r-dec2_r)/2)**2
  b = np.cos(dec1_r)*np.cos(dec2_r)*np.sin(np.abs(ra1_r-ra2_r)/2)**2
  d = 2*np.arcsin(np.sqrt(a+b))
  return np.degrees(d)

# Read data from a catalog bss.dat
# Take RA, DEC coordinates
def import_bss(Fbss):
  cat = np.loadtxt(Fbss, usecols=range(1, 7)) # reads a file into ndarray (NumPy structure); takes only 1-7 columns
  print('The BBS catalog is \n', cat[0]) # checks the first line
  # takes columns with ra(h), ra(m), ra(s) and evaluates ra in degrees 
  ra = 15*(cat[:,0]+cat[:,1]/60+cat[:,2]/3600) 
  # takes columns with dec(grad), dec('), dec(") and evaluates dec in degrees
  dec = np.sign(cat[:,3]) * (abs(cat[:,3]) + cat[:,4]/60 + cat[:,5]/3600)
  obj = list() #preallocates memory
  #for i in range(np.ma.size(cat, axis=0)): 
  for i in range()
    obj.append((i+1, ra[i], dec[i])) # append new line to a list
  return obj # object contains an ID and coordinates


# Read data from a catalog super.csv
def import_super(Fsuper):
  # reads a file into ndarray with specific delimiter; skips first row with header and takes only first two rows
  cat = np.loadtxt(Fsuper, delimiter = ',', skiprows = 1, usecols = [0,1]) 
  print('The BBS catalog is \n', cat[0]) # checks the first line
  # the super.csv already has ra and dec in degrees
  obj = list()
  for i, row in enumerate(cat,1): 
    obj.append((i, row[0], row[1])) # append new line to a list
  return obj

# find the closest distance between the object with coordinates (ra,dec) and compares
# it with every objects in the catalog (cat)
# cat contains tuples of coordinates (ra, dec) in degrees
def find_closest(cat, ra, dec):
  dist = list()
  for obj in cat: # for every object in the catalog
    dist.append(angular_dist(ra, dec, obj[1], obj[2])) # uses function angular_dist
  return (np.argmin(dist)+1, min(dist)) # return ID and value of the minimum distance 
 # NOTE!  np.argmin(dist)+1  to start from the 1 (not 0) object


# Compares two catalogs. Takes coordinates (ra,dec) in degrees from bothes catalogs
# In loops compares objects
# Finds distance that is less then a given offset 
def crossmatch(cat1, cat2, offset):
  match = [] # empty list
  not_match = [] # empty list
  for id1, ra1, dec1 in cat1: # for each row in the first catalog
    closest_dist = np.inf # starts from the biggest distance
    closest_id = None # creates a variable for matched ID
    for id2, ra2, dec2 in cat2: # for each row in the second catalog
      dist = angular_dist(ra1,dec1,ra2,dec2)
      if dist < closest_dist: # sorts the distances and find the smallest
        closest_id2 = id2
        closest_dist = dist
    # Now we have the smallest distance and ID for an objects from the first catalog 
    # Compare this distance with offset to find if two objects crossmath
    if closest_dist < offset:
      # saves IDs of the objects from both catalogs and an angular distance between them
      match.append((id1, closest_id2, closest_dist)) 
    else: 
      # if not match, saves just an ID from the first catalog
      not_match.append((id1))
  return match, not_match

bss_cat = import_bss('/home/dzyga/Docs/Univer_Python/Data/bss.dat') # your file path
super_cat = import_super('/home/dzyga/Docs/Univer_Python/Data/super.csv')


# Now you check and try different offsets
max_dist = 40/3600
matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
print('Matched objects are ', matches[:3])
print('No matches are ', no_matches[:3])
print('Number of no matches is ', len(no_matches))


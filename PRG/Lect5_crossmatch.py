# Write your crossmatch function here.
#import numpy as np
#import time

#def angular_dist(r1, d1, r2, d2):
#  a = np.sin(np.abs(d1 - d2)/2)**2
#  b = np.cos(d1)*np.cos(d2)*np.sin(np.abs(r1 - r2)/2)**2
#  return 2*np.arcsin(np.sqrt(a + b))

"""
# Firt
def crossmatch(cat1, cat2, max_radius):
  start = time.perf_counter()
  max_radius = np.radians(max_radius)
  
  matches = []
  no_matches = []

  # Convert coordinates to radians
  cat1 = np.radians(cat1)
  cat2 = np.radians(cat2)

  for id1, (ra1, dec1) in enumerate(cat1):
    min_dist = np.inf
    min_id2 = None
    for id2, (ra2, dec2) in enumerate(cat2):
      dist = angular_dist(ra1, dec1, ra2, dec2)
      if dist < min_dist:
        min_id2 = id2
        min_dist = dist
        
    # Ignore match if it's outside the maximum radius
    if min_dist > max_radius:
      no_matches.append(id1)
    else:
      matches.append((id1, min_id2, np.degrees(min_dist)))
    
  time_taken = time.perf_counter() - start
  return matches, no_matches, time_taken
"""

"""
# VECTORISATION !!!!!!  
def crossmatch(cat1, cat2, max_radius):
  start = time.perf_counter()
  max_radius = np.radians(max_radius)
  
  matches = []
  no_matches = []

  # Convert coordinates to radians
  cat1 = np.radians(cat1)
  cat2 = np.radians(cat2)
  
  ra2s = cat2[:,0];
  dec2s = cat2[:,1];

  for id1, (ra1, dec1) in enumerate(cat1):
    min_dist = np.inf
    min_id2 = None
    dist = angular_dist(ra1, dec1, ra2s, dec2s)
    for id2, (ra2, dec2) in enumerate(cat2):
      dist = angular_dist(ra1, dec1, ra2, dec2)
      if dist < min_dist:
        min_id2 = id2
        min_dist = dist
        
    # Ignore match if it's outside the maximum radius
    if min_dist > max_radius:
      no_matches.append(id1)
    else:
      matches.append((id1, min_id2, np.degrees(min_dist)))
    
  time_taken = time.perf_counter() - start
  return matches, no_matches, time_taken
"""
  
"""
# Stop at max
def crossmatch(cat1, cat2, max_radius):
  start = time.perf_counter()
  max_radius = np.radians(max_radius)
  
  matches = []
  no_matches = []

  # Convert coordinates to radians
  cat1 = np.radians(cat1)
  cat2 = np.radians(cat2)

  sort_ind = np.argsort(cat2[:, 1])
  cat2_sort = cat2[sort_ind]
  #print('Sorted indexes: ', sort_ind)
  #print('Sorted catalog: ', cat2_sort)
  
  for id1, (ra1, dec1) in enumerate(cat1):
    min_dist = np.inf
    min_id2 = None
    max_dec = dec1 + max_radius
    for id2, (ra2, dec2) in enumerate(cat2_sort):
      if dec2 > max_dec:
        break
        
      dist = angular_dist(ra1, dec1, ra2, dec2)
      if dist < min_dist:
        min_id2 = sort_ind[id2]
        min_dist = dist
        
    # Ignore match if it's outside the maximum radius
    if min_dist > max_radius:
      no_matches.append(id1)
    else:
      matches.append((id1, min_id2, np.degrees(min_dist)))
    
  time_taken = time.perf_counter() - start
  return matches, no_matches, time_taken
#"""

"""
# Binari search!!!!
def crossmatch(cat1, cat2, max_radius):
  print('___Binary search___')
  start_point = time.perf_counter()
  max_radius = np.radians(max_radius)
  
  matches = []
  no_matches = []

  # Convert coordinates to radians
  cat1 = np.radians(cat1)
  cat2 = np.radians(cat2)

  sort_ind = np.argsort(cat2[:, 1])
  cat2_sort = cat2[sort_ind]
  
  for id1, (ra1, dec1) in enumerate(cat1):
    min_dist = np.inf
    min_id2 = None
    
    dec_start = dec1 - max_radius
    print('Start from ', dec_start, ' declanation')
    dec_stop = dec1 + max_radius
    print('Stop at ', dec_stop, ' declanation')
    
    #print(cat2_sort[:,1].searchsorted(dec_start, side='left'))
    #print(cat2_sort[:,1].searchsorted(dec_stop, side='right'))
    
    start = np.searchsorted(cat2_sort[:,1], dec_start, side='left')
    #print(start)
    stop = np.searchsorted(cat2_sort[:,1], dec_stop, side='left')
    #print(stop)
    print('Start index for DEC is ', start)
    print('Value of the start point is ', cat2_sort[start, 1])
    
    for id2, (ra2, dec2) in enumerate(cat2_sort[start:stop]):
      dist = angular_dist(ra1, dec1, ra2, dec2)
      #if dec2 > stop:
      #  break
        
      if dist < min_dist:
        min_id2 = sort_ind[id2]
        min_dist = dist
        
    # Ignore match if it's outside the maximum radius
    if min_dist > max_radius:
      no_matches.append(id1)
    else:
      matches.append((id1, min_id2, np.degrees(min_dist)))
    
  time_taken = time.perf_counter() - start_point
  return matches, no_matches, time_taken

#"""


"""
# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  
  # The example in the question
  ra1, dec1 = np.radians([180, 30])
  cat2 = [[180, 32], [55, 10], [302, -44]]
  cat2 = np.radians(cat2)
  ra2s, dec2s = cat2[:,0], cat2[:,1]
  dists = angular_dist(ra1, dec1, ra2s, dec2s)
  print(np.degrees(dists))
  

  cat1 = np.array([[180, 30], [45, 10], [300, -45]])
  cat2 = np.array([[180, 32], [55, 10], [302, -44]])
  matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
  print('matches:', matches)
  print('unmatched:', no_matches)
  print('time taken:', time_taken)


  # A function to create a random catalogue of size n
  def create_cat(n):
    ras = np.random.uniform(0, 360, size=(n, 1))
    decs = np.random.uniform(-90, 90, size=(n, 1))
    return np.hstack((ras, decs))

  # Test your function on random inputs
  n=150
  np.random.seed(0)
  cat1 = create_cat(n)
  cat2 = create_cat(n)
  matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
  #print('matches:', matches)
  #print('unmatched:', no_matches)
  
  print('Number of Matched objects:', len(matches))
  print('Number of Not Matched objects:', len(no_matches))
  print('time taken:', time_taken)
"""  


#"""
    # ASTROPY and K-D TREES
    
    # Write your crossmatch function here.
import numpy as np
import time
from astropy.coordinates import SkyCoord
from astropy import units as u
    
def crossmatch(cat1, cat2, offs):
    start = time.perf_counter()
      
    matches = []
    no_matches = []
    
    sky_cat1 = SkyCoord(cat1*u.degree, frame='icrs')
    sky_cat2 = SkyCoord(cat2*u.degree, frame='icrs')
      
    print(type(sky_cat1))
    ids, d2d, _ = sky_cat1.match_to_catalog_sky(sky_cat2)
    #print(ids)
    #print(d2d)
    dist = d2d.value
    #print('Minimum distance is ', dist)
    #print('... while offset is ', offs)
    
    for id1, (cl_id, cl_dist) in enumerate(zip(ids,dist)):
        if dist[id1] <= offs:
            matches.append([id1, cl_id, cl_dist])
        else:
            no_matches.append(id1)
    
    time_taken = time.perf_counter() - start
    return matches, no_matches, time_taken
    



# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # The example in the question
  cat1 = np.array([[180, 30], [45, 10], [300, -45]])
  cat2 = np.array([[180, 32], [55, 10], [302, -44]])
  matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
  print('matches:', matches)
  print('unmatched:', no_matches)
  print('time taken:', time_taken)

  # A function to create a random catalogue of size n
  def create_cat(n):
    ras = np.random.uniform(0, 360, size=(n, 1))
    decs = np.random.uniform(-90, 90, size=(n, 1))
    return np.hstack((ras, decs))

  # Test your function on random inputs
  np.random.seed(0)
  cat1 = create_cat(10000)
  cat2 = create_cat(10000)
  matches, no_matches, time_taken = crossmatch(cat1, cat2, 0.5)
  print('matches:', matches)
  print('unmatched:', no_matches)
  print('time taken:', time_taken)


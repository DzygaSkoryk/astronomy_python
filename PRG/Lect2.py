import datetime
print('Hi! What\'s up? \nToday is ', datetime.datetime.now(), ' in UTC \n')

import numpy as np

#Convert coordinates 
def hms2dec(h, m, s):
  return 15*(h + m/60 + s/3600)


def dms2dec(d, m, s):
	dec = np.sign(d)*(abs(d) + m/60 + s/3600)
	return dec


def angular_dist(ra1, dec1, ra2, dec2):

  ra1_r = np.radians(ra1)
  ra2_r = np.radians(ra2)
  dec1_r = np.radians(dec1)
  dec2_r = np.radians(dec2)
  a = np.sin(np.abs(dec1_r-dec2_r)/2)**2
  b = np.cos(dec1_r)*np.cos(dec2_r)*np.sin(np.abs(ra1_r-ra2_r)/2)**2
  d = 2*np.arcsin(np.sqrt(a+b))
  return np.degrees(d)


ra1, dec1 = 21.07, 0.1
ra2, dec2 = 21.15, -8.2

print('Angular distant in radians is: ', angular_dist(ra1, dec1, ra2, dec2))
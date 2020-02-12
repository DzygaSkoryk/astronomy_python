# FITS files
import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
import time

# close all figures 
plt.close('all')

def lingray(x, a=None, b=None):
  """
  Auxiliary function that specifies the linear gray scale.
  a and b are the cutoffs : if not specified, min and max are used
  """
  if a == None:
      a = np.min(x)
  if b == None:
      b = np.max(x)
  return 255.0 * (x-float(a))/(b-a)

def loggray(x, a=None, b=None):
   """
   Auxiliary function that specifies the logarithmic gray scale.
   a and b are the cutoffs : if not specified, min and max are used
   """
   if a == None:
       a = np.min(x)
   if b == None:
       b = np.max(x)
   linval = 10.0 + 990.0 * (x-float(a))/(b-a)
   return (np.log10(linval)-1.0)*0.5 * 255.0

# Read FITS file
def load_fits(Name):
    hdulist = fits.open(Name)
    data = hdulist[0].data
    print(hdulist.info())
    print('Maximum intesity at: ', np.argmax(data))
    print('Maximum intensity: ', np.unravel_index(np.argmax(data), data.shape))
    print('Maximum intensity value: ', np.amax(data))
    
    # Plot the 2D array
    plt.imshow(data, cmap=plt.cm.viridis)
    plt.xlabel('x-pixels')
    plt.ylabel('y-pixels')
    plt.colorbar()
    plt.show()
    
    # return coordinates of the max intensity pxl
    return data, np.unravel_index(np.argmax(data), data.shape) 
  
# Mean of a FITS files
def mean_fits(Files):
    print(Files)
    n = len(Files)
    if n > 0:
        hdulist = fits.open(Files[0])
        data = hdulist[0].data
        for i in range(n):
            hdulist = fits.open(Files[i])
            data += hdulist[0].data
        data_mean = data/n
    return data_mean

# Median of a FITS files
def median_fits(Files):
    n = len(Files)
    if n > 0:
      hdulist = fits.open(Files[0])
      DataCube = hdulist[0].data
      hdulist.close()
      for i in range(1,n):
          hdulist = fits.open(Files[i])
          data = hdulist[0].data
          DataCube = np.dstack((DataCube, data))
    return (np.median(DataCube,axis = 2), DataCube.nbytes/1024)

def lingray(x, a=None, b=None):
  """
  Auxiliary function that specifies the linear gray scale.
  a and b are the cutoffs : if not specified, min and max are used
  """
  if a == None:
      a = np.min(x)
  if b == None:
      b = np.max(x)
  return 255.0 * (x-float(a))/(b-a)

def loggray(x, a=None, b=None):
   """
   Auxiliary function that specifies the logarithmic gray scale.
   a and b are the cutoffs : if not specified, min and max are used
   """
   if a == None:
       a = np.min(x)
   if b == None:
       b = np.max(x)
   linval = 10.0 + 990.0 * (x-float(a))/(b-a)
   return (np.log10(linval)-1.0)*0.5 * 255.0
 
    


# Execution script
if __name__ == '__main__':
    # clear all figures
    plt.close('all')
    
    # your path and file names
    Path = '/home/dzyga/Docs/Univer_Python/Data/FITS images/' 
    Name = Path + '502nmos.fits'
    Name1 = Path + '791wmos копия.fits'
    Data, Max_xy = load_fits(Name)
    #print(Max_xy)
    
    LinData = lingray(Data)
    LogData = loggray(Data)
    
    fig1 = plt.figure()
    plt.imshow(LogData)
    
       
    fig = plt.figure()
    plt.subplot(211)
    plt.imshow(LinData, cmap=plt.cm.viridis)
    plt.subplot(212)
    plt.imshow(LogData, cmap=plt.cm.plasma)
    plt.subplot_tool()
    plt.show()
    
    
    # Create full path to ALL files
    Files = ['image0.fits', 'image1.fits', 'image2.fits', 'image3.fits', 'image4.fits']
    Names = []
    for i in range(len(Files)):
        #print(Path+Files[i])
        Names.append(Path+Files[i])
  
    
    Start_point = time.perf_counter()
    Mean = mean_fits(Names)
    print('Mean of the FITS images is ', Mean[100, 100])
    Median, Memory = median_fits(Names)
    print('Median of the FITS images is ', Median[100, 100])
    print('Memory taken is ', Memory, ' kB')
    print('Elapsed_time is ', time.perf_counter()-Start_point, ' s')
    
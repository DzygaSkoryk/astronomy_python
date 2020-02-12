import numpy as np

def median_bins(data, B):
  mean = np.mean(data)
  std = np.std(data)
    
  # Initialise bins
  first_bin = 0
  histogram = np.zeros(B)
  bin_width = 2*std/B
    
  # Bin values
  for x in data:
    if x < mean - std:
      first_bin += 1 # just count whole first the very left bin
    elif x < mean + std: # we need this data range
      bin = int((x - (mean - std))/bin_width) #count number of a bin
      histogram[bin] += 1
    # Ignore values above mean + std

  return mean, std, first_bin, histogram


def median_approx(data, B):
  # Call median_bins to calculate the mean, std,
  # and bins for the input values
  mean, std, first_bin, histogram = median_bins(data, B)
    	
  # Position of the middle element
  N = len(data)
  mid = (N + 1)/2 # just middle point of the data 

  count = first_bin
  for b, bincount in enumerate(histogram):
    count += bincount
    if count >= mid:
      # Stop when the cumulative count exceeds the midpoint
      break

  width = 2*std/B
  median = mean - std + width*(b + 0.5)
  return median

# You can use this to test your functions.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your functions with the first example in the question.
  print(median_bins([1, 1, 3, 2, 2, 6], 3))
  print(median_approx([1, 1, 3, 2, 2, 6], 3))

  # Run your functions with the second example in the question.
  print(median_bins([1, 5, 7, 7, 3, 6, 1, 1], 4))
  print(median_approx([1, 5, 7, 7, 3, 6, 1, 1], 4))

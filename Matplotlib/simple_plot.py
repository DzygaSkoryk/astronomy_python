import numpy as np 
import matplotlib.pyplot as plt 

print('Hello, World!')

x = np.linspace(0, 10, 1000)
plt.plot(x, np.sin(x))

plt.show()

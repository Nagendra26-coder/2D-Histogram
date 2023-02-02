import matplotlib.pyplot as plt
import numpy as np

#Generating some random data
data = np.random.randn(1000, 5)

#Generating a 2D histogram
plt.hist2d(data[:,0], data[:,1], bins=20)

#Adding the color bgm
plt.colorbar()

#Showing the plot
plt.show()
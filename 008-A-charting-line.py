import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

# print('xpoints:', xpoints)
# print('ypoints:', ypoints)

plt.plot(xpoints, ypoints, 'o')
plt.grid()
# we would normally use show() to display our chart, but this doesn't work
# in our IDE / console, so we need to save the chart as an image.
#plt.show()
plt.savefig('008-A-charting-line.png')
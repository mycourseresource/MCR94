import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])


plt.scatter(x, y)
# plt.grid()
# we would normally use show() to display our chart, but this doesn't work
# in our IDE / console, so we need to save the chart as an image.
#plt.show()
plt.savefig('008-B-charting-line.png')
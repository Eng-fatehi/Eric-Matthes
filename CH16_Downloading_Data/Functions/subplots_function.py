'''
The subplots() function  
It's a convenient way to generate multiple plots within a single figure.
'''


import matplotlib.pyplot as plt

# Create a figure and a grid of subplots (2 rows, 2 columns)
fig, axs = plt.subplots(2, 2)

# Plot on the first subplot (index 0)
axs[0, 0].plot([1, 2, 3, 4], [10, 5, 10, 5])

# Plot on the second subplot (index 1)
axs[0, 1].plot([1, 2, 3, 4], [3, 6, 1, 7])

# Plot on the third subplot (index 2)
axs[1, 0].plot([1, 2, 3, 4], [8, 6, 4, 2])

# Plot on the fourth subplot (index 3)
axs[1, 1].plot([1, 2, 3, 4], [9, 1, 3, 5])

# Display the plots
plt.show()
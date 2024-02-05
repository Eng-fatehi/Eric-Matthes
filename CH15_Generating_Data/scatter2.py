import matplotlib.pyplot as plt 

plt.style.use('seaborn-v0_8')

input_values =[ 1, 2, 3, 4, 5]
squares = [ 1, 4, 9, 16, 25]

fig, ax = plt.subplots()

# scatter instead of plot  # s argument instead linewidth (to set the size  of the dots)
ax.scatter(input_values, squares, s=50 )  


# Set chart title and label axes:
ax.set_title("Square of Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Value", fontsize=14)

# Set size of tick labels:
ax.tick_params(labelsize=14)

plt.show()


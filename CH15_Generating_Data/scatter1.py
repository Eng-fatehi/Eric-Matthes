import matplotlib.pyplot as plt 

plt.style.use('seaborn-v0_8')  #background style

fig, ax = plt.subplots()

# Put scatter instead of plot
ax.scatter(2, 4)

# Set chart title and label axes:
ax.set_title("Square of Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Value", fontsize=14)

# Set size of tick labels:
ax.tick_params(labelsize=14)

plt.show()
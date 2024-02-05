import matplotlib.pyplot as plt 

squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)  # The plot method: to plot the data.

# Set chart title and label axes:
ax.set_title("Square of Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Value", fontsize=14)

# Set size of tick labels:
ax.tick_params(labelsize=14)

plt.show()    # The function plt.showI() opens " Matplotlib's viewer " and displays the plot.
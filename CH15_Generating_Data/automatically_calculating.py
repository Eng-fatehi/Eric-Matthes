''' Calculating Data Automatically '''
import matplotlib.pyplot as plt 

input_value = range (1, 100) # a range of x-value 
squares = [x**2 for x in input_value]  # sauaring each number (x**2), and assigning the results to y_value (squares)

fig, ax = plt.subplots()   # ax is (x,y) axis
ax.scatter(input_value, squares, s=11)

# The axis() method requires four values: the minimum and maximum values ofr the x-axis and the y-axis.
# Its purpose is to adjust the background to match the layout.
# We assume that the values are as follows:
ax.axis([0, 101, 0, 10100])

ax.ticklabel_format(style='plain') # Customizing Tick Labels plain of sci ..ect Page (309 and 310)

plt.show()


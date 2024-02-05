
'''
# Calculating Data Automatically
import matplotlib.pyplot as plt 

input_value = range (1, 100) # a range of x-value 
squares = [x**2 for x in input_value]  # squaring each number (x**2), and assigning the results to y_value (squares)

# The subplots() method: to create a figure and axis ,ax is(x,y) axis 
and fig is a figure that contains a plotting area to plot the data.
# The plot() method: to plot the data.

fig, ax = plt.subplots()   # ax is (x,y) axis

# create a scatter plot:

ax.scatter(input_value, squares, c=squares, cmap=plt.cm.Reds, s=8)  # c is color, cmap is color map, s is size.

# The axis() method requires four values: the minimum and maximum values ofr the x-axis and the y-axis.
# Its purpose is to adjust the background to match the layout.
# We assume that the values are as follows:
ax.axis([0, 101, 0, 10100])
ax.ticklabel_format(style='plain') # Page (309 and 310)

plt.show()

'''



'''
It looks like you've created a range of numbers from 1 to 99. 
If you want to see the contents of this range, 
you can convert it to a list using list():
'''

input_value = range(1, 100)       # The range(1, 100) function generates numbers from 1 to 99, 
input_list = list(input_value)
print(input_list)


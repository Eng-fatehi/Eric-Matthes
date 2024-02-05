''' Error Checking and handle missing data. '''

# First let's run the code to see the headers that are included in this data file:
from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

path = Path('C:\CH/death_valley_2021_simple.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

#for index, colum_header in enumerate(header_row):
    #print(index, colum_header)

''' The high and low temperatures ate at indexes 3 and 4, 
so we'll need to change the indexes in our code to reflect these new positions.'''

# Now let's change the indexes in our code to reflect these new positions:

# Extract dates, high and low temperatures.
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)


# Plot the high temperatures.
plt.style.use('seaborn-v0_8')    # background style is seaborn-v0_8
fig, ax= plt.subplots()         # subplots() function is used to create a figure and axis.
ax.plot(dates, highs, color='red', alpha=0.5)  # plot() function is used to plot the dates and high temp. in the axis.
ax.plot(dates, lows, color= 'blue', alpha=0.5)  
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
# fill_between() method, used to fills the space between the two y values.
# alpha is used to control the transparency of the fill.


# Format plot
ax.set_title("Daily High and LowTemperatures, 2021\nDeat Valley, CA", fontsize=20)
'''
طريقه اخرى لتعريف العنوان
title = "Daily High and LowTemperatures, 2021\nDeat Valley, CA"
ax.set_title(title, fontsize=20)
'''
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()           # to draws the date labels diagonally انحرافي
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()

# ValueError: invalid literal for int() with base 10: '' 
''' The traceback tells us that Python can't process the high temperature for one of the dates
because it can't convert an empty string to ('') into an integer. '''


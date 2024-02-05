
from pathlib import Path # import pathlib modulefor working with paths of the file.
import csv               # for working with CSV files.
import matplotlib.pyplot as plt
from datetime import datetime

# 
path = Path('C:\CH/sitka_weather_07-2021_simple.csv') 
# path = Path('weather_data/sitka_weather_07-2021_simple.csv')

# we can use read_text() method to read the whole file as a string.
lines = path.read_text(encoding='utf-8').splitlines()  
reader = csv.reader(lines)
header_row = next(reader)

reader = csv.reader(lines)
header_row = next(reader)

#for index, column_header in enumerate(header_row, start=1):
    #print(index, column_header)  # column headers رؤس الاعمدة
#print(header_row)

# Extract high temperatures and dates from this file.
highs, dates = [], []
for row in reader :
    current_date = datetime.strptime(row[2], '%Y-%m-%d') 
    # the strptime() method is used to convert the string to a datetime object.
    high = int(row[4])   # the int() function is used to convert the string to a numerical format.
    dates.append(current_date)
    highs.append(high)
#print(highs)
#print(dates)

# Plot the high temperatures.
plt.style.use('seaborn-v0_8')    # background style is seaborn-v0_8
fig, ax= plt.subplots()         # subplots() function is used to create a figure and axis.
ax.plot(dates, highs, color='red')      # plot() function is used to plot the data in the axis.


# Format plot
ax.set_title("Daily high temperatures, July 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()           # to draws the date labels diagonally انحرافي
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()






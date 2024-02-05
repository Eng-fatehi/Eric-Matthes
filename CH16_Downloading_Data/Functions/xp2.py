
from pathlib import Path # import pathlib module for working with paths of the file.
import csv               # for working with CSV files.

# 
path = Path('C:\CH/sitka_weather_07-2021_simple.csv')  #
# path = Path('weather_data/sitka_weather_07-2021_simple.csv')

# we can use read_text() method to read the whole file as a string.
# The Path.read_text reads the contents of the file as a string.
Q = path.read_text() #.splitlines() # path.read_text() is used toreads the contents of the file as a string.
s = csv.reader(Q) # csv.reader() is used to read the contents of the file as a list.
x = next(s)
print(x)
#x = next(s)
#print(x)



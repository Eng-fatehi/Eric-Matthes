
from pathlib import Path # import pathlib modulefor working with paths of the file.
import csv               # for working with CSV files.

# 
path = Path('C:\CH/sitka_weather_07-2021_simple.csv')  #
# path = Path('weather_data/sitka_weather_07-2021_simple.csv')

# we can use read_text() method to read the whole file as a string.
lines = path.read_text(encoding='utf-8').splitlines()  # 
reader = csv.reader(lines)
header_row = next(reader)

reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row, start=1):
    print(index, column_header)  # column headers رؤس الاعمدة
#print(header_row)







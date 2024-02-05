''' cvs.reader() method returns a list where each list is a row (line of data) in the csv file. '''
import csv

# Open the CSV file

with open('C:\CH/sitka_weather_07-2021_simple.csv') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    
    # Iterate through each row in the CSV file
    for row in csv_reader:
        # Each row is a list representing the columns in that row
        print(row)

'''
The csv.reader() 
is a Python function from the csv module used to read CSV (Comma Separated Values) files. 
It allows you to read and parse CSV data into Python data structures (lists), 
making it easier to work with tabular data.
'''
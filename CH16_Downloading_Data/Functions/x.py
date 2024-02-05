""" 


from pathlib import Path # import pathlib module for working with paths of the file.
import csv               # for working with CSV files.

path ='''vmifj
vfmkdfsdfmk
fkrmk'''
line= path.splitlines()
#line.splitlines() 
reader= csv.reader(line)
header_row = next(reader)
print (header_row) """


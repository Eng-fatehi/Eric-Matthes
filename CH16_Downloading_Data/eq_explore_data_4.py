''' Extracting Earthquake Data and Building a World Map.'''
from pathlib import Path
import json
import plotly.express as px # for visualizing data on a world map.

# Read data as a string and convert it to a Python object.
path = Path('C:\CH/eq_data/month.geojson')
contents = path.read_text(encoding='utf-8') 
all_eq_data = json.loads(contents) # json.loads() fucntion is used to convert the string into a python object.

""" 
# Create a more readable version of the data file.
path = Path('C:\CH/eq_data/readable_eq_data.geojson') # 
readable_contents = json.dumps(all_eq_data, indent=4) # json.dumps() function can take an optional indent argument.
path.write_text(readable_contents) # path.write_text() function is used to write the contents of the string to a file.

 """

# Making a List of All Earthquakes.
# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']  # alle earthquakes dictoinaries.
# print(len(all_eq_dicts)) # len() fucntion is used to get ... 

""" 
# Extracting Magnitudes.
mags = []                                  # mags mean magnitudes
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']  
    mags.append(mag)
print(mags[:100])
 """

# Extracting Locations Data.
mags, lons, lats = [],[],[]
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']  
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)


print(mags[:10])
print(lons[:10])
print(lats[:10])


# Building a World Map.
title = 'Global Earthquakes'
fig = px.scatter_geo(lat= lats, lon=lons, size=mags, title=title) 
# The scatter_geo() function used to overlay (a scatterplot of geographic data) on a geographic map.
fig.show()


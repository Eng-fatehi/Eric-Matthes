from pathlib import Path
import json

# Read data as a string and convert it to a Python object.
path = Path('C:\CH/eq_data/month.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents) # json.loads() fucntion is used to convert the string into a python object.

# Making a List of All Earthquakes.
# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']  #The 'features' key contains a list of dictionaries (alle earthquakes dictoinaries).
print(len(all_eq_dicts)) # The len() function returns the number of items (length) in an object.


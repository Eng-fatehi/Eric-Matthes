import json

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# data ={ "name": "John", "age": 30, "city": "New York"}

# Serialize 'data' dictionary to JSON with indentation

json_str = json.dumps(data, indent=4)
print(json_str)


'''
Note:1 
The indent=4 argument tells json.dumps() to use an indentation of 4 spaces. 
This makes the JSON output more human-readable by organizing the data in 
a structured and visually appealing way.

{
    "name": "John",   
    "age": 30,        
    "city": "New York"
}  

'''


''' 
Note:2
If you omit the indent argument or set it to None (which is the default), 
the resulting JSON string will not include any extra whitespace or indentation, making it compact:

json_str_compact = json.dumps(data)
print(json_str_compact)
# Output: {"name": "John", "age": 30, "city": "New York"}

This compact form is often used when space efficiency is important, 
like when transmitting data over networks or storing data in files 
where minimizing space is a priority.
'''
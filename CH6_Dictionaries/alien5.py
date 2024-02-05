""" Using get() """
'''
We can use the get() method to set a default value that will be returned 
if the requested key doesn't exist.
'''
alien_0 = {'color': 'green', 'speed': 'slow'}

#print(alien_0['points']) # Notice (points key) not exist.

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
print(f"points: {point_value}")
 # you get the default value. In this case, points doesn't exist.


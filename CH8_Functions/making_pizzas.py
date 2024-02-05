""" Using get() """
'''
We can use the get() method to set a default value that will be returned 
if the requested key doesn't exist.
'''
alien_0 = {'color': 'green', 'speed': 'slow'}

# print(alien_0['points']) # Notice (points key) not exist.

points = alien_0.get('points', 'No point value assigned.')
print(points)
 # you get the default value. In this case, points doesn't exist.
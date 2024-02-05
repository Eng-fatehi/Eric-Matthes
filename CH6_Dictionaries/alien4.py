""" Modifying Values in a Dictionary """
''' 
An if-elif-else chain determines how far the alien should move to the right,
and assigns this value to the variable x_increment. 
'''

alien_0 = {'x_posítion': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_posítion']}")
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3
# The new position is the old position plus the increment.
alien_0['x_posítion']= alien_0['x_posítion'] + x_increment

print(f"New position: {alien_0['x_posítion']}")


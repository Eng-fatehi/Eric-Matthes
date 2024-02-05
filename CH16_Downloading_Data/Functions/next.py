'''
Python Iterators
An iterator is an object that contains a countable number of values.
'''

'''
Example 1 :
next() and iter() functions wit list
Create an iterator from a list by using next() function, and print the items one by one:
'''

'''
mylist = iter(["apple", "banana", "cherry"]) # iter() method is used to create an iterator object from a list.
x = next(mylist)
print(x)
x = next(mylist)
print(x)
x = next(mylist)
print(x)
'''

'''
Example 2 :
iter() function with a asting.
Create an iterator from a string, and print the items one by one:
'''

'''
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
'''


'''
Example 3:
iter() function with a tuple.
Return an iterator from a tuple, and print each value:

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
'''

# Looping Through an Iterator
# A more elegant( اناقة) way of automatically iterating is by using the for loop.
# We can also use a for loop to iterate through an iterable object:


'''
Example 1:
for loop with a tuple.

Iterate the values of a tuple:
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)
'''

'''
Example 2:
for loop with a string.

Iterate the characters of a string:
mystr = "banana"

for x in mystr:
  print(x)
'''

'''
Other Examples:
iter() function with a list.

# define a list
my_list = [4, 7, 0]

# create an iterator from the list
iterator = iter(my_list)

# get the first element of the iterator
print(next(iterator))  # prints 4

# get the second element of the iterator
print(next(iterator))  # prints 7

# get the third element of the iterator
print(next(iterator))  # prints 0
'''


'''
Other Examples:
Working of for loop for Iterators
    
# create a list of integers
my_list = [1, 2, 3, 4, 5]

# create an iterator from the list
iterator = iter(my_list)

# iterate through the elements of the iterator
for element in iterator:

    # Print each element
    print(element)
'''


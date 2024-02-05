''' The len() function returns the number of items (length) in an object.'''

""" 
# Example 1:

languages = ['Python', 'Java', 'JavaScript']

# compute the length of languages
length = len(languages)
print(length)
 """

# Example 2:

testList = []
print(testList, 'length is', len(testList))           # [] length is 0

testList = [1, 2, 3]
print(testList, 'length is', len(testList))           # [1, 2, 3] length is 3    

testTuple = (1, 2, 3)
print(testTuple, 'length is', len(testTuple))         # (1, 2, 3) length is 3  

testRange = range(1, 10)
print('Length of', testRange, 'is', len(testRange))   # Length of range(1, 10) is 9
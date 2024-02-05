''' splitlines() method return just one list which containing each row (line of data ) from this list one string.'''

#Example:
# This code defines a multi-line string called “para” that contains several lines of text.

para = '''Hello 
Welcome to

Shiksha
Online
'''
print(para.splitlines())

# The splitlines() method returns a list of (the lines in the string, using the newline character as a separator.
# the splitlines() method has separated the original string into a list of many individual lines, 
#removing the line break characters that separated them.

# String without line breaks.
para = """Hello There Welcome to Shiksha Online"""
print(para.splitlines())
'''
enumerate() function التعداد
is used to with loop and keeping track of the index of each item during iteration. 
It returns an enumerate object, which yields pairs containing the index and the value. 

'''

my_list = ['apple', 'banana', 'orange']

for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")


'''
You can also specify a start value for the index by providing a second argument to enumerate()

Example: 

my_list = ['apple', 'banana', 'orange']

for index, value in enumerate(my_list, start=1): # providing a start value for the index which is 1.
    print(f"Index: {index}, Value: {value}")

The output will be:
-----------------------
Index: 1, Value: apple
Index: 2, Value: banana
Index: 3, Value: orange
-----------------------


'''
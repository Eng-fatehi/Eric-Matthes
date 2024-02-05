''' Using try-except blocks'''
# Python can't do this, so we get a traceback, so we go to use try-except blocks .
try: 
    print(5/0)
except ZeroDivisionError:
    print("-------------------------")
    print("You can't divide by zero!")
    print("-------------------------")

''' 
Try-Except block asks Python to run the code in the try block 
and telling it how to respond if there is an exception.
and the user sees a friendly error message instead of a traceback.
'''
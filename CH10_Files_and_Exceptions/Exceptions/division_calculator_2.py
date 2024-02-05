''' Using Exceptions to Prevent Crashes '''

print("\nGive me two numbers, and I'll divide them. ")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:                                                  # 1
        answer = int(first_number) / int(second_number)   
    except ZeroDivisionError:                             # 2
        print("You can't divide by 0!")                   # 3
    else:                                                 # 4
        print(answer)

'''
There are four additions in the program to prevent the program from crashing.
'''
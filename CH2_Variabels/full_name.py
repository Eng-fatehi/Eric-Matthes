first_name = "fatehi"
last_name = "abdo"
full_name = f"{first_name} {last_name}"  # f string
#full_name = first_name+" "+ last_name   # normal string

print(full_name)

# Python will replace each variable with its value.
"""
The f is for format, 
because Python formats the string by replacing the name 
of any variable in braces wiht its value.
"""

print(f"Hello, {full_name.title()}!")  # f-string
print("Hello, "+full_name.title()+"!")   # normal string.

message = f"Hello, {full_name.title()}!"
print(message)
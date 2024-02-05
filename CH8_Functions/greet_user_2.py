""" Display a simple greeting"""
def greet_user(username):
    print("Hello, "+username.title()+"!") 
greet_user("ali")

#f_string:
#print(f"Hello, {username.title()}!") 
#nomral string:
#print("Hello, "+username.title()+"!")

"""full name"""
#def greet_user(first_name, last_name): #definition function   
    #full_name = (f"{first_name} {last_name}")
    #full_name = f"{first_name} {last_name}"
    #full_name = first_name+" "+last_name   
    #print(f"Hello {full_name.title()}!") or #print("Hello "+full_name.title()+" !")
#greet_user('ali', 'abdo') #call function
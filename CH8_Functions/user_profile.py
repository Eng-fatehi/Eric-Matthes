""" Build dictionary containing everything we know about a user. """
# Arbitrary Keyword Arguments

def build_profile(first, last, **user_info):
    print(type(user_info))
    user_info ['first_name'] = first
    user_info ['last_name'] = last
    return user_info
    
user_profile = build_profile('albert','einstein', location = 'amsterdam', field = 'physics')
print(user_profile)


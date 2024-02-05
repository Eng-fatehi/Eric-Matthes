""" Return dictionary of information abut a person."""
def build_person(first_name, last_name, age = None):
  person = {"first":first_name, "last":last_name}   #person = {"first":first_name, "last":last_name, "age":age}
  if age:
    person["age"] = age
  return person
musician = build_person("jimi", "hendrix", age=33 )
print(musician)


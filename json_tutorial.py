import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

# convert into JSON:
person_json = json.dumps(person)
# use different formatting style
person_json2 = json.dumps(person, indent=4, sort_keys=True)
#  person = json.loads(person_json2)
# the result is a JSON string:
print(person_json) 
print(person_json2) 

with open('person.json', 'w') as file:
    json.dump(person, file, indent=4) # you can also specify indent etc...

person = json.loads(person_json)
print(person)
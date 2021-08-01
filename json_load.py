import json
with open('person.json', 'r') as file:
    person = json.load(file)
    print('method 1 return JSON from a file', person)

class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age
user = User('Max', 27)
#
# userJSON = json.dumps(user)  creates an error, 'object of type User is not json serializable
# so we have to do below
# method 2
def encode_user(o):
    if isinstance(o, User):
        # just the key of the class name is important, the value can be arbitrary.
        return {o.__class__.__name__: True, "name":o.name, "age":o.age}
    else:
        raise TypeError(f"Object of type '{o.__class__.__name__}' is not JSON serializable")

# user = 1 + 2 this will print the TypeError
# This won't
userJSON = json.dumps(user, default=encode_user)
print('method 2 return dict', userJSON)

# method 3

from json import JSONEncoder
class UserEncoder(JSONEncoder):

   def default(self, o):
        if isinstance(o, User):
            return{'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)

userJSON = json.dumps(user, cls=UserEncoder)
print('method 3 return dict', userJSON)
# or method 4
userJSON = UserEncoder().encode(user)
print('method 4 returns dict', userJSON)

# method 5

def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct
# load a json string, decode it as type Class user
user = json.loads(userJSON, object_hook=decode_user)
print(type(user))
print('decode method, return dict', user.name)

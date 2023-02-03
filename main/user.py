import json
from collections import namedtuple
from json import JSONEncoder

class User:
    def __init__(self, name, password, email):
        self.name, self.password, self.email

class UserEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__ 
    
def UserDecoder(userDict):
    return namedtuple('X', userDict.keys())(*userDict.values())

user = User("user", "password", "test@email.com")

# dumps() converts to json format
userJson = json.dumps(user, indent=4, cls=UserEncoder)
print(userJson)

# Parse JSON into an object
userObj = json.loads(userJson, object_hook=UserDecoder)

print("After converting JSON Data into custom Python Object: ")
print(userObj.name, userObj.password, userObj.email)


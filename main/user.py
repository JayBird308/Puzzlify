from __future__ import print_function
import json
from collections import namedtuple
from json import JSONEncoder
try:
    from types import SimpleNamespace as Namespace
except ImportError:
    from argparse import Namespace

class Userlogin:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class GameStats:
    def __init__(self, gamesplayed, gamespassed, gamesfailed):
        self.gamesplayed = gamesplayed
        self.gamespassed = gamespassed
        self.gamesfailed = gamesfailed

class UserInfo(Userlogin, GameStats):
    pass

class UserEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__ 
    
def UserDecoder(userDict):
    return namedtuple('X', userDict.keys())(*userDict.values())

userlogin = Userlogin("username", "password", "test@email.com")
userstats = GameStats(10, 8, 2)
user = (userlogin, userstats)

# dumps() converts to json format
userJson = json.dumps(user, indent=4, cls=UserEncoder)
print(userJson)

# Parse JSON into an object
userObj = json.loads(userJson, object_hook=UserDecoder)

# print python object
print("After converting JSON Data into custom Python Object: ")
print(userObj)
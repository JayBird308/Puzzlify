from __future__ import print_function
from collections import namedtuple
from json import JSONEncoder
from databaseConnection import *

try:
    from types import SimpleNamespace as Namespace
except ImportError:
    from argparse import Namespace

class UserAccount:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.key = ""
        self.memGamesPlayed = 0
        self.memHighScore = 0
        self.trizGamesPlayed = 0
        self.trizHighScore = 0
        self.mqGamesPlayed = 0
        self.mqHighScore = 0
        self.slidingGamesPlayed = 0
        self.slidingHighScore = 0

class UserEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__ 
    
def UserDecoder(userDict):
    return namedtuple('Users', userDict.keys())(*userDict.values())

currentLoggedInUser = UserAccount()
tempUser = UserAccount()
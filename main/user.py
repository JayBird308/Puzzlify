from __future__ import print_function
import json
from collections import namedtuple
from json import JSONEncoder
import requests
from databaseConnection import *

try:
    from types import SimpleNamespace as Namespace
except ImportError:
    from argparse import Namespace

class UserAccount:
    def __init__(self, username, password, email, memGamesPlayed, memHighScore, trizGamesPlayed, trizHighScore, mqGamesPlayed, mqHighScore, slidingGamesPlayed, slidingHighScore):
        self.username = username
        self.password = password
        self.email = email
        self.memGamesPlayed = memGamesPlayed
        self.memHighScore = memHighScore
        self.trizGamesPlayed = trizGamesPlayed
        self.trizHighScore = trizHighScore
        self.mqGamesPlayed = mqGamesPlayed
        self.mqHighScore = mqHighScore
        self.slidingGamesPlayed = slidingGamesPlayed
        self.slidingHighScore = slidingHighScore

class UserEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__ 
    
def UserDecoder(userDict):
    return namedtuple('Users', userDict.keys())(*userDict.values())
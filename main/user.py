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
        self.reset()

    def reset(self):
        self.username = ""
        self.password = ""
        self.key = ""
        self.memGamesPlayed = 0
        self.memHighScore = 0
        self.msGamesPlayed = 0
        self.msHighScore = 0
        self.unscrambleGamesPlayed = 0
        self.unscrambleHighScore = 0
        self.slidingGamesPlayed = 0
        self.slidingHighScore = 0


class UserEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def UserDecoder(userDict):
    return namedtuple('Users', userDict.keys())(*userDict.values())

# currentLoggedInUser holds the latest, up to date information of the user's LOCAL data (retrieved when signed in from firebase)
currentLoggedInUser = UserAccount()
#tempUser can use to hold temporary data for the user before pushing it to the currentLoggedInUser object
tempUser = UserAccount()

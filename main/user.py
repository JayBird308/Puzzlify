from __future__ import print_function
from collections import namedtuple
import json
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
        self.advMemHighScore = 0
        self.msGamesPlayed = 0
        self.msHighScore = 0
        self.advMsHighScore = 0
        self.unscrambleGamesPlayed = 0
        self.unscrambleHighScore = 0
        self.advUnscrambleHighScore = 0
        self.slidingGamesPlayed = 0
        self.slidingHighScore = 0
        self.advSlidingHighScore = 0


class UserEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def UserDecoder(userDict):
    return namedtuple('Users', userDict.keys())(*userDict.values())


# currentLoggedInUser holds the latest, up to date information of the user's LOCAL data (retrieved when signed in from firebase)
currentLoggedInUser = UserAccount()
# tempUser can use to hold temporary data for the user before pushing it to the currentLoggedInUser object
tempUser = UserAccount()


def updateUser():
    try:
        userJson_var = json.dumps(
            currentLoggedInUser, indent=4, cls=UserEncoder)
        update_ref = db.reference('userdata/' + currentLoggedInUser.username)
        users_reference = update_ref.child(currentLoggedInUser.key)
        users_reference.set(userJson_var)
    except:
        print('No user signed in')


# Get DB Data for parsing highest scores
DB_Ref = db.reference('userdata')
DB_Data = DB_Ref.get()

# Retrieve Highest and Average Memory Score
memHighestScore = 0
memHighestScorePlayer = None

for player, stats in DB_Data.items():
    for key, value in stats.items():
        player_data = json.loads(value)
        if "memHighScore" in player_data:
            score = player_data["memHighScore"]
            if score > memHighestScore:
                memHighestScore = score
                memHighestScorePlayer = player_data["username"]

advMemHighestScore = 0
advMemHighestScorePlayer = None

# advanced mem stats
for player, stats in DB_Data.items():
    for key, value in stats.items():
        player_data = json.loads(value)
        if "advMemHighScore" in player_data:
            score = player_data["advMemHighScore"]
            if score > advMemHighestScore:
                advMemHighestScore = score
                advMemHighestScorePlayer = player_data["username"]

# Retrieve Highest and Average Minesweeper Score
msHighestScore = 0
msHighestScorePlayer = None

for player, stats in DB_Data.items():
    for key, value in stats.items():
        player_data = json.loads(value)
        if "msHighScore" in player_data:
            score = player_data["msHighScore"]
            if score > msHighestScore:
                msHighestScore = score
                msHighestScorePlayer = player_data["username"]

advMsHighestScore = 0
advMsHighestScorePlayer = None

for player, stats in DB_Data.items():
    for key, value in stats.items():
        player_data = json.loads(value)
        if "advMsHighScore" in player_data:
            score = player_data["advMsHighScore"]
            if score > advMsHighestScore:
                advMsHighestScore = score
                advMsHighestScorePlayer = player_data["username"]

# Retrieve Highest Unscramble Score
unscrambleHighestScore = 0
unscrambleHighestScorePlayer = None

for player, stats in DB_Data.items():
    for key, value in stats.items():
        player_data = json.loads(value)
        if "unscrambleHighScore" in player_data:
            score = player_data["unscrambleHighScore"]
            if score > unscrambleHighestScore:
                unscrambleHighestScore = score
                unscrambleHighestScorePlayer = player_data["username"]

advUnscrambleHighestScore = 0
advUnscrambleHighestScorePlayer = None

for player, stats in DB_Data.items():
    for key, value in stats.items():
        player_data = json.loads(value)
        if "advUnscrambleHighScore" in player_data:
            score = player_data["advUnscrambleHighScore"]
            if score > advUnscrambleHighestScore:
                advUnscrambleHighestScore = score
                advUnscrambleHighestScorePlayer = player_data["username"]



# Retrieve Highest and Average Sliding Score
slidingHighestScore = 0
slidingHighestScorePlayer = None

for player, stats in DB_Data.items():
    for key, value in stats.items():
        player_data = json.loads(value)
        if "slidingHighScore" in player_data:
            score = player_data["slidingHighScore"]
            if score > slidingHighestScore:
                slidingHighestScore = score
                slidingHighestScorePlayer = player_data["username"]

advSlidingHighestScore = 0
advSlidingHighestScorePlayer = None

for player, stats in DB_Data.items():
    for key, value in stats.items():
        player_data = json.loads(value)
        if "advSlidingHighScore" in player_data:
            score = player_data["advSlidingHighScore"]
            if score > advSlidingHighestScore:
                advSlidingHighestScore = score
                advSlidingHighestScorePlayer = player_data["username"]

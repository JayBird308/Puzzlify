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
total_memScore = 0
mem_count = 0

for player, stats in DB_Data.items():
    for key, value in stats.items():
        player_data = json.loads(value)
        if "memHighScore" in player_data:
            score = player_data["memHighScore"]
            total_memScore += score
            mem_count += 1
            if score > memHighestScore:
                memHighestScore = score
                memHighestScorePlayer = player_data["username"]

if mem_count > 0:
    average_score = total_memScore / mem_count
    average_score = int(average_score)
else:
    average_score = 0

print("The highest Memory score is:", memHighestScore)
print("The player with the highest score is:", memHighestScorePlayer)
print("The average Memory High Score is:", average_score)
print('==================================================')

# Retrieve Highest and Average Minesweeper Score
msHighestScore = 0
msHighestScorePlayer = None
total_msScore = 0
ms_count = 0

for player, stats in DB_Data.items():
    for key, value in stats.items():
        player_data = json.loads(value)
        if "msHighScore" in player_data:
            score = player_data["msHighScore"]
            total_memScore += score
            mem_count += 1
            if score > msHighestScore:
                msHighestScore = score
                msHighestScorePlayer = player_data["username"]

if mem_count > 0:
    average_score = total_memScore / mem_count
    average_score = int(average_score)
else:
    average_score = 0

print("The highest Minesweeper score is:", msHighestScore)
print("The player with the highest Minesweeper score is:", msHighestScorePlayer)
print("The average Minesweeper High Score is:", average_score)
print('==================================================')

# Retrieve Highest Unscramble Score
unscrambleHighestScore = 0
unscrambleHighestScorePlayer = None
total_unscrambleScore = 0
unscramble_count = 0

for player, stats in DB_Data.items():
    for key, value in stats.items():
        player_data = json.loads(value)
        if "unscrambleHighScore" in player_data:
            score = player_data["unscrambleHighScore"]
            total_unscrambleScore += score
            unscramble_count += 1
            if score > unscrambleHighestScore:
                unscrambleHighestScore = score
                unscrambleHighestScorePlayer = player_data["username"]

if unscramble_count > 0:
    average_score = total_unscrambleScore / unscramble_count
    average_score = int(average_score)
else:
    average_score = 0

print("The highest Unscramble score is:", unscrambleHighestScore)
print("The player with the highest score is:", unscrambleHighestScorePlayer)
print("The average unscramble High Score is:", average_score)
print('==================================================')

# Retrieve Highest and Average Sliding Score
slidingHighestScore = 0
slidingHighestScorePlayer = None
total_slidingScore = 0
sliding_count = 0

for player, stats in DB_Data.items():
    for key, value in stats.items():
        player_data = json.loads(value)
        if "slidingHighScore" in player_data:
            score = player_data["slidingHighScore"]
            total_memScore += score
            mem_count += 1
            if score > slidingHighestScore:
                slidingHighestScore = score
                slidingHighestScorePlayer = player_data["username"]

if mem_count > 0:
    average_score = total_memScore / mem_count
    average_score = int(average_score)
else:
    average_score = 0

print("The highest Sliding score is:", slidingHighestScore)
print("The player with the highest Sliding score is:", slidingHighestScorePlayer)
print("The average Sliding High Score is:", average_score)
print('==================================================')

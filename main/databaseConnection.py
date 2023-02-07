import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

jsonURL = 'https://puzzlify-74c00-default-rtdb.firebaseio.com/.json'
dbURL = 'https://puzzlify-74c00-default-rtdb.firebaseio.com/'
path = "main\\puzzlify-74c00-firebase-adminsdk-27vsv-55d04e21b4.json"
cred = firebase_admin.credentials.Certificate(path)
firebase_admin.initialize_app(cred, {'databaseURL': dbURL})

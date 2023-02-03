import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = firebase_admin.credentials.Certificate("main\\puzzlify-74c00-firebase-adminsdk-27vsv-55d04e21b4.json")
firebase_admin.initialize_app(cred)

ref = db.reference("https://puzzlify-74c00-default-rtdb.firebaseio.com/")

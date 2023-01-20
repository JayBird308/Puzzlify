from firebase_admin import db


ref = db.reference("https://puzzlify-74c00-default-rtdb.firebaseio.com/")
# Connection String
# connection = pyodbc.connect('DRIVER={SQL Server}; SERVER=MSI\PUZZLIFYINSTANCE;DATABASE=Puzzlify; Trusted_Connection=yes;')

# cursor = connection.cursor()
# cursor.execute("SELECT @@VERSION as version")

# Print connection status
# for i in cursor:
#    print(i)
import pyodbc

# Connection String
connection = pyodbc.connect('DRIVER={SQL Server}; SERVER=MSI\PUZZLIFYINSTANCE;DATABASE=Puzzlify; Trusted_Connection=yes;')

cursor = connection.cursor()
cursor.execute("SELECT @@VERSION as version")

# Print connection status
for i in cursor:
    print(i)
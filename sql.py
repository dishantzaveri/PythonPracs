# import mysql.connector
# mydb = mysql.connector.connect(
# host="localhost",
# user="root",
# password="Moonshine@123",
# )
# print(mydb)

# import mysql.connector
# mydb = mysql.connector.connect(
# host="localhost",
# user="root",
# password="Moonshine@123",
# )
# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE Electronics")

# import mysql.connector
# mydb = mysql.connector.connect(
# host="localhost",
# user="root",
# password="Moonshine@123",
# )
# mycursor = mydb.cursor()
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#     print(x)

# import mysql.connector
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Moonshine@123",
#   database="electronics"
# )

# import mysql.connector
# mydb = mysql.connector.connect(
# host="localhost",
# user="root",
# password="Moonshine@123",
# database="electronics"
# )
# mycursor = mydb.cursor()
# mycursor.execute("""CREATE TABLE Laptop (Id int(11) NOT NULL, Name varchar(250) NOT NULL,Price float NOT NULL,Purchase_date Date NOT NULL,PRIMARY KEY (Id))""")

import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="Moonshine@123",
database="electronics"
)
mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")
for x in mycursor:
 print(x)
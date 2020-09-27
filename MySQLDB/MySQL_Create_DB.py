import mysql.connector

mydb = mysql.connector.connect(

host = "localhost",
user = "root_admin"

)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE college")
# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#     print(x)

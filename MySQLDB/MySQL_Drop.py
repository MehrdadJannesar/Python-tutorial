import mysql.connector as SQLC

database = SQLC.connect(
host = "localhost",
user = "root_admin",
database = "college"
)

cursor = database.cursor()

statement = "DROP TABLE if exists prof"

cursor.execute(statement)

database.close()

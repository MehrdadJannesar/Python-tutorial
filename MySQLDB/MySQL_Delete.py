import mysql.connector as SQLC

database = SQLC.connect(
host = "localhost",
user = "root_admin",
database = "college"
)

cursor = database.cursor()


query = "DELETE FROM student WHERE roll_no = 21"

cursor.execute(query)

database.commit()

database.close()

import mysql.connector as SQLC

database = SQLC.connect(
host = "localhost",
user = "root_admin",
database = "college"
)

cursor = database.cursor()

# UPDATE tb_name SET = "new value" WHERE ="old value"

statement = "UPDATE student SET roll_no = 23 WHERE name = 'Mehrdad'"

cursor.execute(statement)

database.commit()

database.close()

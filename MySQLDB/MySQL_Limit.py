import mysql.connector as SQLC

database = SQLC.connect(
host = "localhost",
user = "root_admin",
database = "college"
)

cursor = database.cursor()

# SELECT * FROM tb_name LIMIT limit
#
# SELECT * FROM tb_name LIMIT OFFSET offset


# query = "SELECT * FROM student LIMIT 2"
query = "SELECT * FROM student LIMIT 0 OFFSET 2"


cursor.execute(query)
res_set = cursor.fetchall()

for item in res_set:
    print(item)

import mysql.connector as SQLC

database = SQLC.connect(
host = "localhost",
user = "root_admin",
database = "college"
)

cursor = database.cursor()


# SELECT col1,col2 FROM tb_name JOIN/INNER JOIN tb_name ON condition
# SELECT col1,col2 FROM tb_name LEFT JOIN tb_name ON condition
# SELECT col1,col2 FROM tb_name RIGHT JOIN tb_name ON condition


# statement = "SELECT S.name FROM student S JOIN prof ON S.roll_no = prof.roll_no"
statement = "SELECT S.name FROM student S RIGHT JOIN prof P ON S.roll_no = P.roll_no"


cursor.execute(statement)

res_set = cursor.fetchall()

for item in res_set:
    print(item)

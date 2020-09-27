import mysql.connector as SQLC

database = SQLC.connect(
host = "localhost",
user = "root_admin",
database = "college"
)

cursor = database.cursor()


# SELECT attr1,attr2,...,attrN FROM tb_name
# SELECT * FROM tb_name


print("Displaying NAME Col from the student table:")

# query = "SELECT name FROM student"
query = "SELECT * FROM student ORDER BY name DESC"


cursor.execute(query)

myres = cursor.fetchall()


for item in myres:
    print(item)

database.close()

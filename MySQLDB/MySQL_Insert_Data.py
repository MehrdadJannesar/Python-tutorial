import mysql.connector as SQLC

database = SQLC.connect(
host = "localhost",
user = "root_admin",
database = "college"
)

cursor = database.cursor()

# INSERT INTO tb_name (col1,col2,...,coln) VALUES (val1,val2,...,valn)
sql = "INSERT INTO prof (name, branch,roll,section,age,roll_no) VALUES (%s, %s,%s, %s,%s, %s)"
val = [("raha", "information tech", 1706254, "IT-3", 21, 20),
("mani", "information tech",1706253,"IT-3",23,25),
("namdar", "information tech",176271,"IT-3",20,30),
("korosh", "computer science",1706273,"IT-2",19,24)
]

cursor.executemany(sql,val)
database.commit()

print(cursor.rowcount, "details inserted")

database.close()

import mysql.connector as SQLC

database = SQLC.connect(
host = "localhost",
user = "root_admin",
database = "college"
)

cursor = database.cursor()


# CREATE TABLE tabel_name(
#
# col_name col_data_type,
# col_name col_data_type,
# col_name col_data_type,
# ....
#
# )



cursor.execute("""

CREATE TABLE prof(

id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(255)


)
""")

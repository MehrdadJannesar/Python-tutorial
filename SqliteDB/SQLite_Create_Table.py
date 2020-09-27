import sqlite3
from sqlite3 import Error

def create_connection(db_file):

    conn = None

    try:
        conn = sqlite3.connect(db_file)
        return conn

    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):

    try:
        c = conn.cursor()
        c.execute(create_table_sql)

    except Error as e:
        print(e)


def main():

    database = r".\SqliteDB\pythonsqlite.db"

    sql_create_projects_tb = """
    CREATE TABLE IF NOT EXISTS projects(

        id integer PRIMARY KEY,
        name text NOT NULL,
        begin_date text,
        end_date text

    )

    """


    sql_create_tasks_tb = """
    CREATE TABLE IF NOT EXISTS tasks(

        id integer PRIMARY KEY,
        name text NOT NULL,
        priority integer,
        project_id integer NOT NULL,
        status_id integer NOT NULL,
        begin_date text NOT NULL,
        end_date text NOT NULL,
        FOREIGN KEY (project_id) REFERENCES projects (id)

    )

    """

    conn = create_connection(database)

    if conn is not None:
        #create projects table
        create_table(conn, sql_create_projects_tb)
        #create tasks table
        create_table(conn,sql_create_tasks_tb)

    else:
        print("Error!")



if __name__ == '__main__':
    main()

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

def insert_projects_tb(conn,projects):

    sql = """
            INSERT INTO projects(name, begin_date, end_date) VALUES
            (?,?,?)
    """

    cur = conn.cursor()
    cur.execute(sql,projects)
    conn.commit()
    return cur.lastrowid


def insert_tasks_tb(conn,tasks):

    sql = """
            INSERT INTO tasks (name, priority, status_id, project_id, begin_date, end_date)
            VALUES (?,?,?,?,?,?)


    """
    cur = conn.cursor()
    cur.execute(sql,tasks)
    conn.commit()
    return cur.lastrowid



def main():
    database = r".\SqliteDB\pythonsqlite.db"

    conn = create_connection(database)

    with conn:

        project = ('Cool App with SQLite & Python', "2020-01-01", "2020-01-30")
        project_id = insert_projects_tb(conn, project)

        tasks_1 = ("Analyze the requirements of the App", 1,1,project_id,"2020-01-01","2020-01-20")
        tasks_2 = ("Confirm with user about the top requirements",1,1,project_id,"2020-01-20","2020-01-30")

        insert_tasks_tb(conn, tasks_1)
        insert_tasks_tb(conn, tasks_2)


if __name__ == '__main__':
    main()

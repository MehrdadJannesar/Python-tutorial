from SQLite_Create_Table import create_connection


def select_all_tasks(conn):

    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_tasks_by_priority(conn, priority):

    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE priority = ?", (priority,))

    rows = cur.fetchall()

    for row in rows:
        print(row)

def main():

    conn = create_connection(r".\SqliteDB\pythonsqlite.db")

    with conn:

        print("1. Query task by priority: ")
        select_tasks_by_priority(conn,1)

        print("2. Query all tasks:")
        select_all_tasks(conn)



if __name__ == '__main__':
    main()

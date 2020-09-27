from SQLite_Create_Table import create_connection

def select_where_like(conn):

    cur = conn.cursor()

    # LIKE 'TE%', '%Hran', '%ra%', Tehran --> Tehr_n

    cur.execute("""

        SELECT
            TrackId,
            name
        FROM
            tracks
        WHERE
            name LIKE '%Wild'

    """)

    rows = cur.fetchall()

    for row in rows:
        print(row)


def main():

    conn = create_connection(r".\SqliteDB\chinook.db")

    with conn:
        print("Query:")
        select_where_like(conn)

if __name__ == '__main__':
    main()

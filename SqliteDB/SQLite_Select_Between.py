from SQLite_Create_Table import create_connection

def select_where_between(conn):

    cur = conn.cursor()
    cur.execute("""

            SELECT
                InvoiceId,
                BillingAddress,
                InvoiceDate,
                Total
            FROM
                invoices
            WHERE
                InvoiceDate BETWEEN '2010-01-01' AND '2010-01-31'

            ORDER BY
                InvoiceDate

    """)

    rows = cur.fetchall()

    for row in rows:
        print(row)

def main():

    conn = create_connection(r".\SqliteDB\chinook.db")

    with conn:

        print("Query:")
        select_where_between(conn)

if __name__ == "__main__":
    main()

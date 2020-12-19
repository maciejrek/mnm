import psycopg2


def connect_to_db():
    conn = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="db", port="5432")
    print("connected :)")
    return conn


def create_table():
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS MY_TABLE")
    cur.execute(
        '''CREATE TABLE MY_TABLE
          (ID SERIAL PRIMARY KEY     NOT NULL,
          NUMBER1            INT     NOT NULL,
          NUMBER2            INT     NOT NULL,
          RESULT            INT     NOT NULL);'''
    )
    print("Table created successfully")
    conn.commit()
    conn.close()

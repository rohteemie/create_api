import sqlite3


def db_connection():
    """Function to create connection to the database

    Returns:
        _type_: _Return a connection object_
    """
    conn = sqlite3.connect("user.sqlite")
    return conn


conn = db_connection()

cursor = conn.cursor()
query = """CREATE TABLE IF NOT EXISTS workers(
    id integer PRIMARY KEY,
    name text NOT NULL,
    age integer NOT NULL,
    gender text NOT NULL,
    email text NOT NULL
)"""

# execution the sql query in the database using the cursor
cursor.execute(query)

# commit the changes made in the databses and it's table.
conn.commit()
# close the database connection once it has serve it purposes.
conn.close()

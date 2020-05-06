import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    # create a database connection to a persistant DB  
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
        
    return conn


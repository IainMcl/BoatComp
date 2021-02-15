import sqlite3
import sys
from decouple import config


def init(DB: str):
    create_connection(DB)


def create_connection(db_file: str):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

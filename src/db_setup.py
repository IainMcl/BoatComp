import sqlite3
import sys
from decouple import config


def init(DB: str):
    """Data base setup. To be run once on initial start.

    :param DB: File path to sqlite3 database.
    :type DB: str

    :return: None
    :rtype: None
    """
    create_connection(DB)


def create_connection(db_file: str):
    """Establish database connecton.

    :para, df_file: File path to sqlite3 database.
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

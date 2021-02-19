import sqlite3
import sys
from decouple import config
from settings import DB_PATH
from typing import TypeVar, Type


""" Context managing db connection

In some cases it is desierable to leave a connection open for example with speed
of writing data. However, in most cases it is important to close the connection
to prevent the connection remaining open during a crash.

For example:

```python
import sqlite3

with sqlite3.connect("<database>.db") as connection:
    res = connection.execute("SELECT name FROM sqlite_master")
```

The use of the context manager will ensure that the connection is always closed
no mater the exit type.

"""


def create_table(table_name: str, fields: list[tuple[str, str]], db: str = DB_PATH) -> None:
    """
    Creates a new table in a sqlite3 database.

    :param table_name: Name of the table to be created.
    :type table_name: str
    :param fields: Data fields for the table. These should 
            be of the form of a list of tuples containing the name of the 
            variable and the type of the variable as a string.
            fields = [
                ("field1", "INTEGER"),
                ("field2", "TEXT"),
                ("field3", "NULL"),
                ("field4", "REAL"),
                ("field5", "BLOB")
            ]
    :type fields: list[tuple[str, str]]
    :param db: Path to sqlite database. Defaults to DB_PATH, defaults to DB_PATH
    :type db: str, optional
    :raises ValueError: If input fields types are not valid sqlite3 data types.
    """
    types: list[str] = [
        "INTEGER",
        "REAL",
        "TEXT",
        "NULL",
        "BLOB"
    ]

    with sqlite3.connect(db) as conn:
        cur = conn.cursor()
        string: str = ""
        for field in fields:
            if field[1].upper() not in types:
                raise ValueError(f"""
                    Data type {field[1]} is not a sqlite3 data type.
                """)
            string += f"{field[0]} {field[1]}, "
        # remove comma from the last
        string = string[:-2]
        cur.execute(f"""
            CREATE TABLE IF NOT EXISTS { table_name } (
                { string }
            )
        """)
        conn.commit()


# Type of table contents.
# This could be of the form
#   (int, str, str, bool)
# For something like id, posx, posy, in_use
# T = TypeVar("T")


def insert_one(table_name: str, values: tuple[str, ...], db: str = DB_PATH) -> None:
    """
    Insert values into a new row in the database table.

    :param table_name: Table name within database.
    :type table_name: str
    :param values: Tuple of values to be added to the row of the database.
    :type values: tuple[str, ...]
    :param db: Path to sqlite database, defaults to DB_PATH
    :type db: str, optional
    """

    string: str = ", ".join(map(str, values))
    with sqlite3.connect(db) as conn:
        cur = conn.cursor()
        cur.execute(f"""
            INSERT INTO {table_name} VALUES (
                {string}
            )
        """)


def main() -> None:
    create_table("Iains", [("type", "TEXT"), ("loc", "INTEGER")])


if __name__ == "__main__":
    main()

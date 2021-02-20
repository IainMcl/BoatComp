import sqlite3
import sys
from decouple import config
from settings import DB_PATH
from typing import TypeVar, Type


class Table():
    """
    Sqlite3 database table.

    Used as a base class for database entries.
    """

    def __init__(self, table_name: str, fields: list[tuple[str, str]], db: str = DB_PATH) -> None:
        """
        Create a table within a database 'db'.

        :example: marks = Table("marks", [
                                          "posx", "REAL",
                                          "posy", "REAL",
                                          "type", "TEXT"
                                          ])

        :param table_name: Name of table in database.
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
        :param db: Path to sqlite database, defaults to DB_PATH
        :type db: str, optional
        :raises ValueError: If input fields are not valid sqlite3 data types.
        """
        self._table_name = table_name
        self._fields = fields
        self._db = db

        types: list[str] = [
            "INTEGER",
            "REAL",
            "TEXT",
            "NULL",
            "BLOB"
        ]
        # Create the table
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

    def get_field_names(self) -> list[str]:
        """
        Get a list of the field names available within the table.

        :return: List of names that can be selected from the database table.
        :rtype: list[str]
        """
        return [x[0] for x in self._fields]

    def get_field_types(self) -> list[str]:
        return [x[1] for x in self._fields]

    def insert_one(self, values: tuple[str, ...]) -> None:
        """
        Insert values into a new row in the database table.

        :param values: Tuple of values to be added to the row of the database.
        :type values: tuple[str, ...]
        """

        string: str = ", ".join(map(str, values))
        with sqlite3.connect(self.db) as conn:
            cur = conn.cursor()
            cur.execute(f"""
                INSERT INTO {self.table_name} VALUES (
                    {string}
                )
            """)
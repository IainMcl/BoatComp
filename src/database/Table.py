import sqlite3
import sys
from decouple import config
import pandas as pd
from settings import DB_PATH
from typing import TypeVar, Type, Union, Any

list_or_single = Union[tuple[str, ...], list[tuple[str, ...]]]


class Table():
    """
    Sqlite3 database table.

    Used as a base class for database entries with functionality to interact 
    with the database in common ways, so as to reduce the chance of invalid SQL
    errors.
    """

    def __init__(self, table_name: str, fields: list[tuple[str, str]], db: str = DB_PATH, schema: Union[str, None] = None) -> None:
        """
        Create a table within a database 'db'.

        :example: marks = Table("marks", [
                  ("posx", "REAL"),
                  ("posy", "REAL"),
                  ("type", "TEXT")
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
        for field in fields:
            if not field[1].isupper():
                raise ValueError(
                    f"Field types must be upper case. Raised on {field}.")
        if not fields:
            # Catch empty fields before trying to input to db
            raise ValueError(f"Fields can not be empty. Passed {fields}")
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
                        Data type {field[1].upper()} is not a sqlite3 data type.
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

    def get_field_names(self, as_string: bool = False) -> Union[list[str], str]:
        """
        Get a list of the field names available within the table.

        :param as_string: If the return is to be a python list or a comma 
            separated string. True: string, False list, defaults to False.
        :type as_string: bool
        :return: List of names that can be selected from the database table. Or
            if as_string then as string comma separated list.
            'arg1, arg2, arg3'
        :rtype: Union[list[str], str]
        """
        names = [x[0] for x in self._fields]
        if not as_string:
            return names
        else:
            return ", ".join(names)

    def get_field_types(self) -> list[str]:
        """
        Get a list of database field types.
        These can be one of the 5 sqlite3 data types:
        * REAL
        * TEXT
        * INTEGER
        * NULL
        * BLOB  

        :return: List of data types in the order they appear in the table.
        :rtype: list[str]
        """
        return [x[1] for x in self._fields]

    def get_fields(self) -> list[tuple[str, str]]:
        """
        Get a list of all table fields and their sqlite3 data types.


        :example:
            > fields = get_fields()
            > print(fields)
            >>> [("name1", "INTEGER"), ("name2", "REAL"), ...]

        :return: List of all values and their types.
        :rtype: list[tuple[str, str]]
        """
        return self._fields

    def insert_one(self, values: tuple[Any, ...]) -> None:
        """
        Insert values into a new row in the database table.

        :param values: Tuple of values to be added to the row of the database.
        :type values: tuple[Any, ...]
        """

        if not self._check_values(values):
            raise ValueError(f"Values are not of the correct format. {values}")

        string: str = ", ".join(map(str, values))
        names = self.get_field_names(as_string=True)
        with sqlite3.connect(self._db) as conn:
            cur = conn.cursor()
            cur.execute(f"""
                INSERT INTO {self._table_name} ({names}) VALUES (
                    {string}
                )
            """)
        cur.commit()

    def insert_many(self, values_list: list[tuple[Any, ...]]) -> None:
        """
        Insert a list of tuples into the database table.

        :param values_list: List of tuples containing a new row of data to be 
            input.
        :type values_list: list[tuple[Any, ...]]
        :raises ValueError: If the values are of the wrong length or type to be 
            input.
        """
        if not self._check_values(values_list):
            raise ValueError(
                f"Values are not of the correct format. {values_list}")
        names = self.get_field_names(as_string=True)
        with sqlite3.connect(self._db) as conn:
            cur = conn.cursor()
            cur.executemany(f"""
                INSERT INTO {self._table_name} ({names}) VALUES (
                    {("?, "*len(self._fields))[:-2]}
                )
            """, values_list)
        cur.commit()

    def _check_values(self, values: list_or_single) -> bool:
        """
        Check the values to be inserted into the database are of the correct 
            length and type to be added to the table.

        Current checks:
            - Check the length of each tuple matches the number of cols in table.
            - Check each data type matches the table expected input type.

        :param values: List of tuple containing entries, or single tuple
            containing data.
        :type values: list_or_single
        :raises ValueError: If not list or tuple.
        :return: True if checks pass, else False.
        :rtype: bool
        """
        # Length check
        if type(values) == list:
            length: int = len(self._fields)
            for val in values:
                if len(val) != length:
                    return False
        elif type(values) == tuple:
            if len(values) != length:
                return False
        else:
            raise ValueError("Incorrect type to be added to table.")

        types: list[str] = self.get_field_types()

        # If tuple, make a list so indexing works with checks.
        if type(values) == tuple:
            values = [values]

        for row in values:
            for i in range(types):
                if type == "INTEGER" and type(row[i]) != int:
                    return False
                if type == "NULL" and row[i]:
                    # If not null or none or False
                    return False
                if type == "TEXT" and type(row[i]) != str:
                    return False
                if type == "REAL" and (type(row[i]) != int or type(row[i]) != float):
                    return False

        return True

    def select_all(self, as_df: bool = True) -> Union[pd.DataFrame, list[tuple[Any]]]:
        """
        Select all data from the table as either a list of tuples or a pandas df.

        :param as_df: True if return type should be pd.DataFrame, defaults to True
        :type as_df: bool, optional
        :return: All data as pd.DataFrame if as_df == True else list[tuple[Any]]
        :rtype: Union[pd.DataFrame, list[tuple[Any]]]
        """
        query = f"""
            SELECT * FROM {self._table_name}
            """
        with sqlite3.connect(self._db) as conn:
            if as_df:
                data = pd.read_sql_query(query, conn)
            else:
                cur = conn.cursor()
                cur.execute(query)
                data = cur.fetchall()
        return data

    # def update_one(self, id: int, values: tuple[Any]):
        # with sqlite3.connect(self._db) as conn:
        #cur = conn.cursor()
        # cur.execute(f"""
        # UPDATE {self._table_name}
        # SET {self.get_field_names(as_string=True)}
        # WHERE
        # """)

import sqlite3
import sys
from decouple import config
from settings import DB_PATH


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


def create_table(table_name: str, fields: list[tuple[str, str]], db: str = DB_PATH) -> bool:
    with sqlite3.connect(db) as conn:
        cur = conn.cursor()
        string = ""
        for field in fields:
            string += f"{field[0]} {field[1]}, "
        # remove comma from the last
        string = string[:-2]
        cur.execute(f"""
            CREATE TABLE IF NOT EXISTS { table_name } (
                { string }
            )
        """)
        conn.commit()


def main():
    create_table("Iains", [("type", "TEXT"), ("loc", "INTEGER")])


if __name__ == "__main__":
    main()

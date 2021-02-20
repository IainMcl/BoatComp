from database.Table import Table
import os


def test_instantiation() -> None:
    t = Table("test_table", fields=[
        ("arg1", "Integer"),
        ("arg2", "REAL"),
        ("arg3", "NULL"),
        ("arg4", "TEXT"),
        ("arg5", "BLOB")
    ], db="./test.db")

    assert os.path.exists("test.db")
    assert '_table_name' in t.__dir__()
    assert '_fields' in t.__dir__()
    assert '_db' in t.__dir__()

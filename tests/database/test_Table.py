from database.Table import Table
import os
import pytest
from typing import Type


@pytest.fixture
def create_table():
    """
    Generate a basic Table instance using all 5 data types.

    :return: Database table.
    :rtype: Type[Table]
    """
    t: Type[Table] = Table("test_table", fields=[
        ("arg1", "INTEGER"),
        ("arg2", "REAL"),
        ("arg3", "NULL"),
        ("arg4", "TEXT"),
        ("arg5", "BLOB")
    ], db="./test.db")
    return t


@pytest.fixture
def table_with_content() -> Type[Table]:

    return Table()


def test_instantiation(create_table) -> None:
    """
    Test the instantiation has created the instance variables correctly.

    :param create_table: Table test setup
    :type create_table: Type[Table]
    """
    assert os.path.exists("test.db")
    assert '_table_name' in create_table.__dir__()
    assert create_table._table_name == "test_table"
    assert '_fields' in create_table.__dir__()
    assert len(create_table._fields) == 5
    assert '_db' in create_table.__dir__()
    assert create_table._db == "./test.db"


def test_get_field_names(create_table) -> None:
    """
    Test field names can be retrieves as input in constructor.

    :param create_table: pytest.fixtrue of an instantiated Table class.
        t: Type[Table] = Table("test_table", fields=[
            ("arg1", "INTEGER"),
            ("arg2", "REAL"),
            ("arg3", "NULL"),
            ("arg4", "TEXT"),
            ("arg5", "BLOB")
        ], db="./test.db")
    :type create_table: pytest.fixture
    """
    fields: list[str] = create_table.get_field_names()
    assert "arg1" in fields
    assert "arg2" in fields
    assert "arg3" in fields
    assert "arg4" in fields
    assert "arg5" in fields
    assert len(fields) == 5


def test_get_field_names_as_string(create_table) -> None:
    """
    Note: This is giving an error of unexpected key word argument 'as_string'
        No idea why as it is working in every other form of test I have done.

    Test the as_string functionality of Table.get_field_names.
    The args are expected to be returned in a comma separated string.

    :param create_table: pytest.fixture   
        t: Type[Table] = Table("test_table", fields=[

                ("arg1", "INTEGER"),
                ("arg2", "REAL"),
                ("arg3", "NULL"),
                ("arg4", "TEXT"),
                ("arg5", "BLOB")
            ], db="./test.db")
    :type create_table: pytest.fixtrue
    """
    fields = create_table.get_field_names(as_string=True)
    #fields: str = create_table.get_field_names(as_string=True)
    assert type(fields) == str
    assert fields == "arg1, arg2, arg3, arg4, arg5"


def test_get_field_types(create_table) -> None:
    types: list[str] = create_table.get_field_types()
    assert "INTEGER" in types
    assert "NULL" in types
    assert "TEXT" in types
    assert "REAL" in types
    assert "BLOB" in types
    assert "RANDOMTYPE" not in types
    assert len(types) == 5


def test_get_fields() -> None:
    pass


def test_insert_one(create_table) -> None:
    values = ("8", "-36.78", "")
    # create_table.insert_one()


def test_insert_many() -> None:
    pass


def test_select_all() -> None:
    pass


def test_check_values() -> None:
    pass

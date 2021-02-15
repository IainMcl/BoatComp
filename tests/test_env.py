from db_setup import init
from decouple import config
from settings import DB


def test_env():
    assert("Hello" == "Hello")


def test_con():
    init(DB)

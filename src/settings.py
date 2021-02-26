import os
from decouple import config

ROOT_DIR: str = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH: str = os.path.join(ROOT_DIR, 'configuration.conf')

DB_PATH: str = os.path.join(ROOT_DIR, config("DB", default="boatcomp.db"))

# Environment variables
DEBUG: bool = True
DB: str = config("DB", default="boatcomp.db")


def check_setup():
    """Checks setup config.
    """
    pass

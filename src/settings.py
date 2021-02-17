import os
from decouple import config

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(ROOT_DIR, 'configuration.conf')

DB_FILE = os.path.join(ROOT_DIR, config("DB"))

# Environment variables
DEBUG = True
DB = config("DB")


def check_setup():
    """Checks setup config.
    """
    pass

import os


LEN_SHORT_ID = 6
MAX_LEN_CUSTOM_ID = 16
MAX_LEN_ORG_LINK = 2083
PATTERN = '[a-zA-Z0-9]*$'


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')

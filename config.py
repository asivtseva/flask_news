from dotenv import dotenv_values
from os import urandom


class Config:
    SECRET_KEY = urandom(16).hex()
    SQLALCHEMY_DATABASE_URI = dotenv_values('.env')['DATABASE_URI']
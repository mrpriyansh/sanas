from os import environ

class Config:
    DATABASE_URI = environ.get("DATABASE_URI")
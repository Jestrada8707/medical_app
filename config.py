import urllib.parse

password = urllib.parse.quote_plus('postgres')
SQLALCHEMY_DATABASE_URI = f'postgresql://postgres:{password}@localhost/hh_db'

class Config:
    DEBUG = True
    SECRET_KEY = 'd1b32f8b73ba4f9e9bf6756c9e2bb969'
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

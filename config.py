class Config:
    DEBUG = True
    SECRET_KEY = 'd1b32f8b73ba4f9e9bf6756c9e2bb969'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/hh_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

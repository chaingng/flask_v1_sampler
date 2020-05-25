class Config(object):
    DEBUG = False
    TESTING = False
    DB_SERVER = '192.168.1.56'

class ProductionConfig(Config):
    DB_SERVER = '192.168.19.32'

class DevelopmentConfig(Config):
    DB_SERVER = 'localhost'
    DEBUG = True

class TestingConfig(Config):
    DB_SERVER = 'localhost'
    DEBUG = True
    DATABASE_URI = 'sqlite:///:memory:'
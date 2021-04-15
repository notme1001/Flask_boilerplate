import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False

# set database development and production ex: "mysql://username:password@hostname:3306/database_name"
class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'default': DevelopmentConfig,
    'mongo_uri': "mongodb://localhost:27017/todo_db",
    'jwt-secret-string': 'Secret',
    'database': 'secret'
}
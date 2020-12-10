import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False

# set database development and production ex: "mysql://username:password@hostname:3306/database_name"
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql://username:password@hostname:3306/database_name"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mysql://root:@localhost:3306/comdb"

config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'default': DevelopmentConfig,
}
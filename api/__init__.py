from flask import Flask
from flask_bcrypt import Bcrypt
from env import config
from flask_jwt_extended import JWTManager
from pymongo import MongoClient 

server = MongoClient(config['mongo_uri']) 
db = server[config['database']] 
jwt = JWTManager()
fbcrypt = Bcrypt()

def myApp(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    app.config['JWT_SECRET_KEY'] = config['jwt-secret-string']
    jwt.init_app(app)
    app.config['JWT_BLACKLIST_ENABLED'] = True
    app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

    fbcrypt.init_app(app)

    # set version api
    from .v1 import api as v1_blueprint
    app.register_blueprint(v1_blueprint, url_prefix='/api/v1')

    return app

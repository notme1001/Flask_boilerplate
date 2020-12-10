from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import ModelSchema
from flask_bcrypt import Bcrypt
from env import config
from flask_jwt_extended import JWTManager
    
db = SQLAlchemy()
ml = ModelSchema
jwt = JWTManager()
fbcrypt = Bcrypt()

def myApp(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    @app.before_first_request
    def create_tables():
        db.create_all()

    app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
    jwt.init_app(app)
    app.config['JWT_BLACKLIST_ENABLED'] = True
    app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

    db.init_app(app)
    fbcrypt.init_app(app)

    # set version api
    from .v1 import api as v1_blueprint
    app.register_blueprint(v1_blueprint, url_prefix='/api/v1')

    return app

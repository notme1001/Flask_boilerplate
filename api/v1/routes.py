from __future__ import print_function
from flask_restful import Api
from . import api
from .. import jwt
from .resources import auth, todo
from ..models.blacklist import Blacklist
from . import views

api = Api(api, catch_all_404s=True)

# User resources 
@jwt.token_in_blacklist_loader
def check_token(decrypted_token):
    jti = decrypted_token['jti']
    return Blacklist.jti_blacklisted(jti)

api.add_resource(auth.UserRegistration, '/registration')
api.add_resource(auth.UserLogin, '/login')
api.add_resource(auth.UserLogoutAccess, '/logout/access')
api.add_resource(auth.UserLogoutRefresh, '/logout/refresh')
api.add_resource(auth.TokenRefresh, '/token/refresh')
api.add_resource(auth.AllUsers, '/users')
api.add_resource(auth.SecretResource, '/secret')

# Todo Resources
api.add_resource(todo.TodoGetdata, '/get')
api.add_resource(todo.TodoPostData, '/post')
api.add_resource(todo.DeleteTodo, '/delete/<int:id>')
api.add_resource(todo.UpdateTodo, '/update/<int:id>')
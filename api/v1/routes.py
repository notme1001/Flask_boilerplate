from __future__ import print_function
from flask_restful import Api
from . import api
from .. import jwt
from .resources import auth, todo
from . import views
from .models.blacklist import Blacklist

api = Api(api, catch_all_404s=True)

# User resources 
@jwt.token_in_blacklist_loader
def check_token(decrypted_token):
    jti = decrypted_token['jti']
    return Blacklist.jti_blacklisted(jti)

api.add_resource(auth.UserLogin, '/login')
api.add_resource(auth.UserRegistration, '/register')
api.add_resource(auth.UserLogoutAccess, '/logout')
api.add_resource(auth.TokenRefresh, '/refresh/token')

# Todo
api.add_resource(todo.TodoPostData, '/create/todo')
api.add_resource(todo.UpdateTodo, '/edit/todo/<string:title>')
api.add_resource(todo.DeleteTodo, '/delete/todo/<string:title>')
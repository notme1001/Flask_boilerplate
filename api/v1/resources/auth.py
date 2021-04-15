from flask_restful import Resource, reqparse
from ...helper.encrypt import Encrypt
from ..models.Users import Users
from ..models.blacklist import Blacklist
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
import datetime

parser = reqparse.RequestParser()
parser.add_argument('username', help = 'This field cannot be blank', required = True)
parser.add_argument('password', help = 'This field cannot be blank', required = True)

class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()
        
        if Users.find_user(data['username']):
            return {'message': 'User {} already exists'.format(data['username'])}
        
        new_user = {
            'username': data['username'],
            'password': Encrypt.hash_password(data['password'])
        }

        try:
            user = Users.createUser(new_user)
            return {
                'message': 'User {} was created'.format(data['username']),
            }
        except:
            return {'message': 'Something went wrong'}, 500


class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        current_user = Users.find_user(data['username'])

        if not current_user:
            return {'message': 'User {} doesn\'t exist'.format(data['username'])}
        if Encrypt.check_password(current_user['password'], data['password']):
            expires = datetime.timedelta(days=3)
            access_token = create_access_token(identity = data['username'], expires_delta=expires)
            refresh_token = create_refresh_token(identity = data['username'], expires_delta=expires)
            return {
                'message': 'Logged in as {}'.format(current_user['username']),
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        else:
            return {'message': 'Wrong credentials'}


class UserLogoutAccess(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = Blacklist.create(jti)
            return {'message': 'Access token has been revoked'}
        except:
            return {'message': 'Something went wrong'}, 500


class UserLogoutRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = Blacklist.create(jti)
            return {'message': 'Refresh token has been revoked'}
        except:
            return {'message': 'Something went wrong'}, 500


class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity = current_user)
        return {'access_token': access_token}

class SecretResource(Resource):
    @jwt_required
    def get(self):
        return {
            'Message': "Unlocked"
        }
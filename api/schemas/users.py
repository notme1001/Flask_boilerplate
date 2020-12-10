from .. import ml, db
from ..models.users import Users
from marshmallow import fields

class UserSchema(ml):
    
    class Meta(ml.Meta):
        model = Users
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    username = fields.String(required=True)
    password = fields.String(required=True)

user_schema = UserSchema()
users_schema = UserSchema(many=True)
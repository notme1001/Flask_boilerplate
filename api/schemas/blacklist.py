from .. import ml, db
from ..models.blacklist import Blacklist
from marshmallow import fields

class BlacklistSchema(ml):
    
    class Meta(ml.Meta):
        model = Blacklists
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    jti = fields.String(required=True)

blacklist_schema = BlacklistSchema()
blacklists_schema = BlacklistSchema(many=True)
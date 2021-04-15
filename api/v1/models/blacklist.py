from ... import db
from ...helper.scheme import Scheme

col = db['blacklist'] 
blacklist_schema = {
    'jti': {
        'type': 'string',
        'required': True,
    }
}

class Blacklist():
    Scheme.createTable(blacklist_schema, db, 'blacklist')
    
    @classmethod
    def create(cls, jti):
       return col.insert_one({'jti' : jti})

    @classmethod
    def jti_blacklisted(cls, jti):
        return col.find_one({
            'jti': jti
        })
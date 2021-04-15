from ... import db
from ...helper.scheme import Scheme

col = db['todo'] 
todo_schema = {
    'title': {
        'type': 'string',
        'required': True,
    },
    'description': {
        'type': 'string',
        'required': False,
    }
}

class Todo():
    Scheme.createTable(todo_schema, db, 'todo')
    
    @classmethod
    def create(cls, datajson):
       return col.insert_one(datajson)

    @classmethod
    def findOne(cls, title):
       return col.find_one({'title':title})

    @classmethod
    def deleteById(cls, title):
        col.delete_many({'title': title})

    @classmethod
    def updateById(cls, title, data):
        return col.update_one(
            {'title': str(title)},
            {'$set': {'description': data['description']}}
        )
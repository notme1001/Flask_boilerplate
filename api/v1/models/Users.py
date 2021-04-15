from ... import db

col = db['user'] 

class Users():
    @classmethod
    def find_user(cls, username):
        return col.find_one({'username':username})
    @classmethod
    def createUser(cls, data):
        return col.insert_one(data)
from .. import db

# documentation for sqlalchemy MODELS https://flask-sqlalchemy.palletsprojects.com

class Todo(db.Model):
    __tablename__ = "todos"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    description = db.Column(db.String(128))

    def create(self):
      db.session.add(self)
      db.session.commit()
      return self
    def __init__(self,title,description):
        self.title = title
        self.description = description
    
    @classmethod
    def updateById(cls, id, data):
        try:
            get_todo = cls.query.filter_by(id = str(id)).first()
            if data.get('title'):
                get_todo.title = data['title']
            if data.get('description'):
                get_todo.description = data['description']
            db.session.add(get_todo)
            db.session.commit()
            return get_todo
        except:
            return {'message': 'Something went wrong'}

    @classmethod
    def deleteById(cls, id):
        try:
            num_rows_deleted = cls.query.filter_by(id = str(id)).delete()
            db.session.commit()
            return {'message': '{} row deleted'.format(num_rows_deleted)}
        except:
            return {'message': 'Something went wrong'}
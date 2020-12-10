from .. import db, fbcrypt

# documentation for sqlalchemy MODELS https://flask-sqlalchemy.palletsprojects.com

class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(120), nullable = False)

    def create(self):
      db.session.add(self)
      db.session.commit()
      return self
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def __repr__(self):
        return '' % self.id

    @classmethod
    def find_user(cls, username):
        return cls.query.filter_by(username = username).first()

    @classmethod
    def return_all(cls):
        def to_json(x):
            return {
                'username': x.username,
                'password': x.password
            }
        return {'users': list(map(lambda x: to_json(x), Users.query.all()))}

    @classmethod
    def delete_by_id(cls, id):
        try:
            num_rows_deleted = db.session.query(cls).delete(id)
            db.session.commit()
            return {'message': '{} row(s) deleted'.format(num_rows_deleted)}
        except:
            return {'message': 'Something went wrong'}

    @staticmethod
    def hash_password(password):
        return fbcrypt.generate_password_hash(password).decode('utf-8')

    @staticmethod
    def check_password(dbpassword, password):
        return fbcrypt.check_password_hash(dbpassword, password)
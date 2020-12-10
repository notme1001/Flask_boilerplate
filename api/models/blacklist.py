from .. import db

class Blacklist(db.Model):
    __tablename__ = 'blacklist'
    id = db.Column(db.Integer, primary_key = True)
    jti = db.Column(db.String(120))
    
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
    def __init__(self,jti):
        self.jti = jti
    
    @classmethod
    def jti_blacklisted(cls, jti):
        query = cls.query.filter_by(jti = jti).first()
        return bool(query)
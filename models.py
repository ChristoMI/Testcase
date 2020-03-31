from app import db

class Authorization(db.Model):
    __tablename__ = 'authorization'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, email, passowrd):
        self.email = email
        self.password = password

    def __repr__(self):
        return '<id {}>'.format(self.id)


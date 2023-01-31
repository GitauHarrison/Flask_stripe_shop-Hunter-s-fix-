from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    items = db.relationship('Item', backref='seller', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    price = db.Column(db.Integer, index=True)
    adjustable_quantity = db.Column(db.Boolean)

    def __repr__(self):
        return '<Item {}>'.format(self.name)
from __init__ import db
from flask_login import UserMixin

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String(15),nullable=False)
    last_name=db.Column(db.String(15))
    email = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(300), nullable=False)
    def __repr__(self):
        return f"User('{self.id}', '{self.email}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(40), db.ForeignKey('user.email'), nullable=False)
    task = db.Column(db.String(120), nullable=False)
    description= db.Column(db.Text, nullable=False)
    def __repr__(self):
        return f"Post('{self.task}', '{self.description}')"
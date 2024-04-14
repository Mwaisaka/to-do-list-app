from config import db 
from sqlalchemy_serializer import SerializerMixin


class Todo(db.Model, SerializerMixin):
    __tablename__ = 'todos'
     
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255))
    complete = db.Column(db.Boolean)
     
    def __repr__(self):
        return self.text
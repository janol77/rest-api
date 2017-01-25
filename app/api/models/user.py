from app.db import db
from task import Task


class User(db.Document):
    name = db.StringField(required=True)
    password = db.StringField(required=True)
    email = db.StringField(required=True)
    tasks = db.ListField(db.ReferenceField(Task))

    def serialize(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'tasks': [t.serialize() for t in self.tasks]
        }

from app.db import db


class User(db.Document):
    name = db.StringField(required=True)
    password = db.StringField(required=True)
    email = db.StringField(required=True)

    def serialize(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'email': self.email
        }

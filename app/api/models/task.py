from app.db import db


class Task(db.Document):
    description = db.StringField(required=True)
    title = db.StringField(required=True)

    def serialize(self):
        return {
            'id': str(self.id),
            'description': self.description,
            'title': self.title
        }

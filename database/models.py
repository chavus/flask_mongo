from database.db import db


class Director(db.Document):
    name = db.StringField(required=True)
    country = db.StringField(required=True)


class Movie(db.DynamicDocument):
    name = db.StringField(required=True, unique=True)
    casts = db.ListField(db.StringField(), required=True)
    genres = db.ListField(db.StringField(), required=True)
    director = db.ReferenceField(Director)

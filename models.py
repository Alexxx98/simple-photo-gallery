from sqlalchemy.dialects.postgresql import ARRAY
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()


class Image(db.Model):
    __tablename__ = "Image"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=True)
    added_at = db.Column(db.DateTime(timezone=True), server_default=datetime.now())


class Album(db.Model):
    __tablename__ = "Album"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), default=datetime.now(), nullable=False)
    images = db.Column(ARRAY(db.LargeBinary), nullable=False)
    created_at = db.Cloumn(db.DateTime(timezone=True), server_default=datetime.now())


    def __str__(self):
        return f'Titile: {self.title}, id: {self.id}'

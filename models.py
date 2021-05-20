import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


DB_PATH = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)

db = SQLAlchemy()

# sets up the database
def setup_db(app, database_path=DB_PATH):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    #db.create_all()


# Movies table
class Movies(db.Model):
    __tablename__ = 'movies'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    release_date = db.Column(db.String(120), nullable=False)
    actors = db.relationship('Actors', backref='person', lazy=True)

    def insert(self):
        db.session.add(self)
        db.session.commit()


    def update(self):
        db.session.commit()


    def delete(self):
        db.session.delete(self)
        db.session.commit()


    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date
        }


# Actors table
class Actors(db.Model):
    __tablename__ = 'actors'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(120), nullable=False)
    movies_id = db.Column(
        db.Integer,
        db.ForeignKey('movies.id'),
        nullable=False)


    def insert(self):
        db.session.add(self)
        db.session.commit()


    def update(self):
        db.session.commit()


    def delete(self):
        db.session.delete(self)
        db.session.commit()


    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'movies_id': self.movies_id
        }

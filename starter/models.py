import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:password123@localhost:5432/capstone'

class Movies(db.Model):
    id = db.Column(db.integer, primary_key=True)
    title = db.Column(db.string(120), unique=True, nullable=False)
    release_date = db.Column(db.Datetime, nullable=False)

class Actors(db.Model):
    id = db.Column(db.integer, primary_key=True)
    name = db.Column(db.string(120), nullable=False)
    age = db.Column(db.integer, nullable=False)
    gender = db.Column(db.string(120), nullable=False)

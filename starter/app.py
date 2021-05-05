import os
import json

from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

from models import setup_db, Movies, Actors, db


def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  migrate = Migrate(app, db)

  actor1 = Actors(name='Vin Diesel', age=53, gender='Male', movies_id=1)
  actor1.insert()

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  return app




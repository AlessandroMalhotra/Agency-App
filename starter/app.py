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
  
  
  @app.route('/movies', methods=['GET'])
  def show_movies():
    all_movies = Movies.query.all()

    if all_movies None:
      abort(404)

    movies = [movie.format() for movie in all_movies]
    
    return jsonify({
      'success': True,
      'movies': movies
    }), 200
  
  
  
  
  
  
  
  
  
  
  
  
  return app




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


    @app.route('/movies/create', methods=['POST'])
    def create_movies():
      req = request.get_json()
      new_title = req.get('title')
      new_release_date = req.get('release_date')

      try:
        new_movie = Movies(title=new_title, release_date=new_release_date)
        new_movie.insert()

        return jsonify({
          'success': True,
          'new_movie': [new_movie.format()]
        }), 200
      
      except BaseException:
        abort(400)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    ''' Error Handlers '''
    @app.errorhandler(404)
    def not_found(error):
      return jsonify({
        'success': False,
        'error': 404
        'message': 'Not Found'
      }), 404

    
    @app.errorhandler(400)
    def bad_request(error):
      return jsonify({
        'success': False,
        'error': 404,
        'message': 'Bad Request'
      }), 400
  
  
  
  
  
  
  
  
  
  
  
  return app




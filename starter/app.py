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

    if all_movies is None:
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

    
    @app.route('/movies/<int:id>', methods=['DELETE'])
    def delete_movies(id):
      delete_movie = Movies.query.get(id=id)
      
      if delete_movie is None:
        abort(404)
      
      try:
        delete_movie.delete()

        return jsonify({
          'success': True,
          'movies': id
        }), 200


      except BaseException:
        abort(422)
    

    @app.route('/movies/<int:id>', methods=['PATCH'])
    def update_movies(id):
      req = request.get_json()
      new_title = req.get('title')
      new_release_date = req.get('release_date')
      
      update_movie = Movies.query.get(id=id)

      if update_movie is None:
        abort(404)
      
      try:
        update.title = new_title
        update.release_date = new_release_date

        update_movie.update()

        return jsonify({
          'success': True,
          'movies': [update_movie.format()]
        }), 200

      except BaseException:
        abort(422)
      
  
  @app.route('/actors', methods=['GET'])
  def show_actors():
    all_actors = Actors.query.all()

    if all_actors is None:
      abort(404)
    
    actors = [actor.format() for actor in all_actors]

    return jsonify({
      'success': True,
      'actors': actors
    }), 200

  
  @app.route('/actors/create', methods=['POST'])
  def create_actors():
    req = request.get_json()
    new_name = req.get('name')
    new_age = req.get('age')
    new_gender = req.get('gender')
    new_movie_id = req.get('movie_id')

    try:
      new_actor = Actors(name=new_name, age=new_age, gender=new_gneder, movie_id=new_movie_id)
      new_actor.insert()

      return jsonify({
        'success': True,
        'new_actor': [new_actor.format()]
      }), 200
    
    except BaseException:
      abort(400)



    
    
    
    
    
    
    
    
    
    
    
    
    
    ''' Error Handlers '''
    
    @app.errorhandler(404)
    def not_found(error):
      return jsonify({
        'success': False,
        'error': 404,
        'message': 'Not Found'
      }), 404

    
    @app.errorhandler(400)
    def bad_request(error):
      return jsonify({
        'success': False,
        'error': 404,
        'message': 'Bad Request'
      }), 400
    

    @app.errorhandler(422)
    def unprocessable(error):
      return jsonify({
        'success': False,
        'error': 422,
        'message': 'Unprocessable'
      }), 422
  
  
  
  
  
  
  
  
  
  
  
  return app




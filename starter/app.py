import os
import json

from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

from models import setup_db, Movies, Actors, db
from auth import AuthError, requires_auth


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    migrate = Migrate(app, db)
    CORS(app)


    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-control-Allow-Headers',
            'Content-Type, Authorization')
        response.headers.add(
            'Access-control-Allow-Methods',
            'GET, POST, PATCH, DELETE, OPTIONS')
        return response


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


    @app.route('/movies/<int:id>/delete', methods=['DELETE'])
    def delete_movies(id):
        delete_movie = Movies.query.get(id)

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


    @app.route('/movies/<int:id>/update', methods=['PATCH'])
    def update_movies(id):
        req = request.get_json()
        new_title = req.get('title')
        new_release_date = req.get('release_date')

        update_movie = Movies.query.get(id)

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


    @app.route('/movies/<int:id>', methods=['GET'])
    def show_ind_movie(id):
        movies = Movies.query.get(id)
        movie_actors = db.session.query(Movies, Actors).join(Actors).\
            filter(movies.id == Actors.movies_id).\
            all()

        if movie_actors is None:
            abort(404)

        movie_and_actors = []
        for movie, actors in movie_actors:
            movie_and_actors.append({
                'actor_name': actors.name,
                'actor_age': actors.age,
                'release_date': movie.release_date,
                'title': movie.title
            })

        return jsonify({
            'success': True,
            'movie and actors': movie_and_actors
        }), 200


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
        new_movie_id = req.get('movies_id')

        try:
            new_actor = Actors(
                name=new_name,
                age=new_age,
                gender=new_gender,
                movies_id=new_movie_id)
            new_actor.insert()

            return jsonify({
                'success': True,
                'new_actor': [new_actor.format()]
            }), 200

        except BaseException:
            abort(400)


    @app.route('/actors/<int:id>/delete', methods=['DELETE'])
    def delete_actor(id):
        remove_actor = Actor.query.get(id)

        if remove_actor is None:
            abort(404)

        try:
            remove_actor.delete()

            return jsonify({
                'success': True,
                'id': id
            }), 200

        except BaseException:
            abort(422)


    @app.route('/actors/<int:id>/update', methods=['PATCH'])
    def update_actor(id):
        req = request.get_json()
        update_name = req.get('name')
        update_age = req.get('age')
        update_gender = req.get('gender')
        update_movie_id = req.get('movie_id')

        update_actor = Actors.query.get(id).one_or_none()

        if update_actor is None:
            abort(404)

        try:
            update_actor.name = update_name
            update_actor.age = update_age
            update_actor.gender = update_gender
            update_actor.movie_id = update_movie_id

            update_actor.update()

            return jsonify({
                'success': True,
                'updated_actor': [update_actor.format()]
            }), 200

        except BaseException:
            abort(422)


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
            'error': 400,
            'message': 'Bad Request'
        }), 400

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'Unprocessable'
        }), 422

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'Method not allowed'
        }), 405

    return app

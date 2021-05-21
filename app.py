import os
import json

from flask import(
    Flask, 
    request, 
    abort, 
    jsonify
)
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

    # setting response headers
    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-control-Allow-Headers',
            'Content-Type, Authorization, true')
        response.headers.add(
            'Access-control-Allow-Methods',
            'GET, POST, PATCH, DELETE, OPTIONS')
        return response


    @app.route('/', methods=['GET'])
    def index():
        return jsonify({'message': 'Welcome to My Agency Application'})
    

    ''' Display all the movies '''
    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def show_movies(payload):
        all_movies = Movies.query.order_by(Movies.id).all()

        if all_movies is None:
            abort(404)

        movies = [movie.format() for movie in all_movies]

        return jsonify({
            'success': True,
            'movies': movies
        }), 200


    ''' Create new movie '''
    @app.route('/movies/create', methods=['POST'])
    @requires_auth('post:movies/create')
    def create_movies(payload):
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
            abort(405)
        
        finally:
            db.session.close()


    ''' Delete movies '''
    @app.route('/movies/<int:id>/delete', methods=['DELETE'])
    @requires_auth('delete:movies/delete')
    def delete_movies(payload,id):
        try:
            delete_movie = Movies.query.filter_by(id=id).one_or_none()

            if delete_movie is None:
                abort(404)

        
            delete_movie.delete()

            return jsonify({
                'success': True,
                'movies': id
            }), 200

        except BaseException:
            abort(422)
        
        finally:
            db.session.close()


    ''' Update movies '''
    @app.route('/movies/<int:id>/update', methods=['PATCH'])
    @requires_auth('patch:movies/update')
    def update_movies(payload, id):
        update_movie = Movies.query.filter_by(id=id).one_or_none()

        req = request.get_json()

        if update_movie is None:
            abort(404)

        try:
            new_title = req.get('title')
            new_release_date = req.get('release_date')
            update_movie.title = new_title
            update_movie.release_date = new_release_date

            update_movie.update()

            return jsonify({
                'success': True,
                'movies': [update_movie.format()]
            }), 200

        except BaseException:
            abort(400)


    ''' Display movies with corresponsing actors '''
    @app.route('/movies/<int:id>/individual', methods=['GET'])
    @requires_auth('get:movies/individual')
    def show_ind_movie(payload, id):
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


    ''' Get all actors '''
    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def show_actors(payload):
        all_actors = Actors.query.order_by(Actors.id).all()

        if all_actors is None:
            abort(404)

        actors = [actor.format() for actor in all_actors]

        return jsonify({
            'success': True,
            'actors': actors
        }), 200


    ''' Create new actor '''
    @app.route('/actors/create', methods=['POST'])
    @requires_auth('post:actors/create')
    def create_actors(payload):
        req = request.get_json()
        
        new_name = req.get('name')
        new_age = req.get('age')
        new_gender = req.get('gender')
        new_movie_id = req.get('movies_id')

        try:
            new_actor = Actors(name=new_name, age=new_age, gender=new_gender, movies_id=new_movie_id)
            new_actor.insert()

            return jsonify({
                'success': True,
                'new_actor': [new_actor.format()]
            }), 200

        except BaseException:
            abort(405)
        
        finally:
            db.session.close()


    ''' Delete actors by id '''
    @app.route('/actors/<int:id>/delete', methods=['DELETE'])
    @requires_auth('delete:actors/delete')
    def delete_actor(payload, id):
        try:
            remove_actor = Actors.query.filter_by(id=id).one_or_none()

            if remove_actor is None:
                abort(404)

            remove_actor.delete()

            return jsonify({
                'success': True,
                'id': id
            }), 200

        except BaseException:
            abort(422)
        
        finally:
            db.session.close()


    ''' Update individual actor '''
    @app.route('/actors/<int:id>/update', methods=['PATCH'])
    @requires_auth('patch:actors/update')
    def update_actor(payload, id):
        update_actor = Actors.query.filter_by(id=id).one_or_none()

        if update_actor is None:
            abort(404)
        
        req = request.get_json()

        try:
            update_name = req.get('name')
            update_age = req.get('age')
            update_gender = req.get('gender')
            update_movie_id = req.get('movie_id')
            
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
            abort(400)
        
        finally:
            db.session.close()


    ''' Error Handlers '''

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Resource Not Found'
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
            'error': 405,
            'message': 'Method not allowed'
        }), 405
    

    @app.errorhandler(AuthError)
    def handle_auth_error(ex):
        response = jsonify(ex.error)
        response.status_code = ex.status_code
        return response
    
    
    return app

app = create_app()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
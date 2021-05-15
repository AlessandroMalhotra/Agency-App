import os
import unittest
import json

from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Movies, Actors

DB_HOST = os.getenv('DB_HOST', '127.0.0.1:5432')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'password123')
DB_NAME = os.getenv('DB_NAME', 'capstone_test')


class CapstoneTestCase(unittest.Testcase):
    
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = 'capstone_test'
        self.database_path = "postgres://{}:{}@{}/{}".format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)
        setup_db(self.app, self.database_path)
    
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
        
        self.new_movie = {'title': 'John Wick Chapter 2',
        'release_d ': '2017'}
    

    def tearDown(self):
        pass


    def test_get_all_movies(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
    

    def test_404_get_all_movies(self):
        res = self.client().get('/movies?page=1000', json={'title': 'Cinderella'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource Not Found')

    
    def test_create_movie(self):
        res = self.client().post('/movies/create', json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['new_movie'])
    

    def test_400_create_movie_bad_request(self):
        res = self.client().post('/movies/create/100', json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 400)
        self.assertEqual(data['message'], 'Bad Request')

    
    def test_delete_movie(self):
        res = self.client().delete('/movies/1/delete')
        data = json.loads(res.data)
        movie = Movies.query.filter(Movies.id==1).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['movies'], 1)
        self.assertEqual(movie, None)
    

    def test_422_movie_does_not_exist(self):
        res = self.client().delete('/movies/4/delete')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 422)
        self.assertEqual(data['message'], 'Unprocessable')
    

    def test_update_movie(self):
        res = self.client().patch('/movies/1/update', json={'release_date': '2016'})
        data = json.loads(res.data)
        movies = Movies.query.filter(Movies.id==1).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(movies.format()['release_date'], 1)
    

    def test_422_for_failed_update(self):
        res = self.client().patch('/movies/5/update')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 422)
        self.assertEqual(data['message'], 'Unprocessable')
    

    def test_get_all_actors(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])
    

    def test_404_get_all_actors(self):
        res = self.client().get('/actors?page=1000', json={'name': 'John'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource Not Found')
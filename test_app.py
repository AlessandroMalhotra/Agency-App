import os
import unittest
import json

from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

from app import create_app
from models import setup_db, Movies, Actors

DB_HOST = os.getenv('DB_HOST', '127.0.0.1:5432')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'password123')
DB_NAME = os.getenv('DB_NAME', 'capstone_test')

load_dotenv()

CASTING_ASSISTANT = os.environ.get('CASTING_ASSISTANT_JWT')
CASTING_DIRECTOR = os.environ.get('CASTING_DIRECTOR_JWT')
EXECUTIVE_PRODUCER = os.environ.get('EXECUTIVE_PRODUCER_JWT')


class CapstoneTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = 'capstone_test'
        self.database_path = 'postgresql://{}:{}@{}/{}'.format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)
        setup_db(self.app, self.database_path)
    
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)

            self.db.create_all()

        
        self.new_movie = {
            'title': 'Fast and Furious 6',
            'release_date': '2017'
            }

        self.new_actor = {
            'name': 'Bennedict Cumberbatch',
            'age': 27,
            'gender': 'Male',
            'movies_id': 2
        }
    

    def tearDown(self):
        pass

    
    def test_get_all_movies(self):
        res = self.client().get('/movies', headers={'Authorization': f"Bearer {CASTING_ASSISTANT}"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
    

    def test_404_get_all_movies(self):
        res = self.client().get('/movies/?page=1000', headers={'Authorization': f"Bearer {CASTING_ASSISTANT}"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource Not Found')
    

    
    def test_create_movie(self):
        res = self.client().post('/movies/create', json=self.new_movie, headers={'Authorization': f"Bearer {CASTING_DIRECTOR}"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['new_movie'])
    
    
    
    def test_400_create_movie_bad_request(self):
        res = self.client().post('/movies/create', json={'titles': 'Lion King', 'release_date': 1}, headers={'Authorization': f"Bearer {CASTING_DIRECTOR}"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 400)
        self.assertEqual(data['message'], 'Bad Request')

    
    def test_delete_movie(self):
        res = self.client().delete('/movies/23/delete', headers={'Authorization': f"Bearer {CASTING_DIRECTOR}"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['movies'], 23)
    

    def test_422_movie_does_not_exist(self):
        res = self.client().delete('/movies/6/delete', headers={'Authorization': f"Bearer {CASTING_DIRECTOR}"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 422)
        self.assertEqual(data['message'], 'Unprocessable')
    

    def test_update_movie(self):
        res = self.client().patch('/movies/3/update', json={'title': 'the social network', 'release_date': '2016'}, headers={'Authorization': f"Bearer {EXECUTIVE_PRODUCER}"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
    

    def test_422_for_failed_update(self):
        res = self.client().patch('/movies/6/update', json={'title': 'The Rat Race', 'release_date': '2017'}, headers={'Authorization': f"Bearer {EXECUTIVE_PRODUCER}"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'Resource Not Found')
    

    def test_get_all_actors(self):
        res = self.client().get('/actors', headers={'Authorization': f"Bearer {CASTING_ASSISTANT}"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])
    

    def test_404_get_all_actors(self):
        res = self.client().get('/actors/?page=1000', headers={'Authorization': f"Bearer {CASTING_ASSISTANT}"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource Not Found')
    
    
    def test_create_actor(self):
        res = self.client().post('/actors/create', json=self.new_actor, headers={'Authorization': f"Bearer {CASTING_DIRECTOR}"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['new_actor'])
    
    
    def test_400_create_actor_bad_request(self):
        res = self.client().post('/movies/create', json={'names': 'Daniel Craig', 'age': '43', 'gender': 'male', 'movies_id': 1}, headers={'Authorization': f"Bearer {CASTING_DIRECTOR}"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 400)
        self.assertEqual(data['message'], 'Bad Request')
    

    def test_delete_actor(self):
        res = self.client().delete('/actors/12/delete', headers={'Authorization': f"Bearer {EXECUTIVE_PRODUCER}"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['id'], 12)
    

    def test_422_actor_does_not_exist(self):
        res = self.client().delete('/actors/6/delete', headers={'Authorization': f"Bearer {CASTING_DIRECTOR}"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 422)
        self.assertEqual(data['message'], 'Unprocessable')
    

    def test_update_actors(self):
        res = self.client().patch('/actors/2/update', json={'name': 'Paul Walker', 'age': 45, 'gender': 'male', 'movies_id': 1}, headers={'Authorization': f"Bearer {EXECUTIVE_PRODUCER}"})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['updated_actor'])
    

    def test_422_for_failed_update(self):
        res = self.client().patch('/actors/1/update', json={'name': 'Jimmy Bob', 'age': '24', 'gender': 'male', 'movies_id': 1}, headers={'Authorization': f"Bearer {EXECUTIVE_PRODUCER}"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'Resource Not Found')

    
if __name__ == "__main__":
    unittest.main() 
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
    

    def tearDown(self):
        pass


    def get_all_movies(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
import os
import unittest
import json

from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Movies, Actors


class AppTestCase(unittest.Testcase):
    

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = 'capstone_test'
        self.database_path = "postgres://{}:{}@{}/{}".format()
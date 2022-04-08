from application import app
import application.routes
from flask_testing import TestCase
from unittest.mock import patch
from flask import url_for 

class TestBase(TestCase):
    def create_app(self):
        return app

class TestView(TestBase):
    @patch('application.routes.choice', return_value='Prawn Mayo Sandwich')
    def test_get_main_prawnmayo(self, mock_func):
        response = self.client.get(url_for('get_mains'))
        self.assert200(response)
        self.assertIn(b'Prawn Mayo Sandwich', response.data)

    @patch('application.routes.choice', return_value='KFC Ricebox')
    def test_get_main_KFC(self, mock_func):
        response = self.client.get(url_for('get_mains'))
        self.assert200(response)
        self.assertIn(b'KFC Ricebox', response.data)
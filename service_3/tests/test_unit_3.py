from application import app
import application.routes
from flask_testing import TestCase
from unittest.mock import patch
from flask import url_for 

class TestBase(TestCase):
    def create_app(self):
        return app

class TestView(TestBase):
    @patch('application.routes.choice', return_value='Fruit Bowl')
    def test_get_side_FruitBowl(self, mock_func):
        response = self.client.get(url_for('get_side'))
        self.assert200(response)
        self.assertIn(b'Fruit Bowl', response.data)

    @patch('application.routes.choice', return_value='Apple Slices')
    def test_get_side_AppleSlices(self, mock_func):
        response = self.client.get(url_for('get_side'))
        self.assert200(response)
        self.assertIn(b'Apple Slices', response.data)
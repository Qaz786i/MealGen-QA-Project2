from application import app, db
from application.models import Make_meal
from flask import url_for
import requests_mock
from flask_testing import TestCase
import pytest

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db',
            DEBUG = True
        )
        return app

def setUp(self):
    sample_meal = Make_meal(main='KFC Ricebox', side='Fruit Bowl', prices={'KFC Ricebox':7, 'Fruit Bowl':2}, total_price=9)
    db.create_all()
    db.session.add(sample_meal)
    db.session.commit()

    
    def tearDown(self):
        db.session.remove()
        db.drop_all


class TestView(TestBase):
    def test_frontend(self):
        with requests_mock.Mocker() as m:
            m.get('http://service_2:5000/get-mains', json={"main":"Tuna Mayo Baguette"}) 
            m.get('http://service_3:5000/get-side', json={"side":"Pineapple Chunks"}) 
            m.post('http://service_4:5000/post-meal', json={"price_main":3, "price_side":2, "total_price":5})
            response = self.client.get(url_for('index'))
            self.assert200(response)
            self.assertIn('Mains: KFC Ricebox £7, Sides: Fruit Bowl £2, Total Price: £9', response.data)
            self.assertIn('Mains: Tuna Mayo Baguette £3, Sides: Pineapple Chunks £2, Total Price: £5', response.data)
            


def test_hist_get(self):
        response = self.client.get(url_for('history'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Human', response.data)
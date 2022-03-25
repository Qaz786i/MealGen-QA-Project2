from application import app
from flask_testing import TestCase
from flask import url_for

class TestBase(TestCase):
    def create_app(self):
        return app


class TestResponse(TestBase):
    def test_get_meal(self):
        for main in prices['main_dish']:
            for side in prices['side_dish']:
                result = {'main_dish':main, 'side_dish':side}
                response = self.client.post(url_for('post_meal'), json=result)
                self.assert200(response)
                expect_price = prices['main_dish'][main] + prices['side_dish'][side]
                self.assertEqual(response.json, expect_price)

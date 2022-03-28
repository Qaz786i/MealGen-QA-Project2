from application import app
from application.routes import prices
from flask_testing import TestCase
from flask import url_for

class TestBase(TestCase):
    def create_app(self):
        return app


class TestResponse(TestBase):
    def test_get_meal(self):
           
        








#for main in prices['g_mains']:
            #for side in prices['side']:
                #result = {'main_dish':main, 'side_dish':side}
                #response = self.client.post(url_for('post_meal'), json=result)
                #self.assert200(response)
                #expect_price = prices['main_dish'][main] + prices['side'][side]
                #self.assertEqual(response.json, expect_price)

        
        
        

        
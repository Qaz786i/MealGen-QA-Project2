from application import app
from application.routes import prices
from flask_testing import TestCase
from flask import url_for
from unittest.mock import patch
import pytest

class TestBase(TestCase):
    def create_app(self):
        return app


class TestResponse(TestBase):
    def test_get_meal(self):
        pass
       
        
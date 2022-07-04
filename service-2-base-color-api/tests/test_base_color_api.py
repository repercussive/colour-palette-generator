from application_2 import app
from flask import url_for
from flask_testing import TestCase

class TestBase(TestCase):
  def create_app(self):
      return app

class TestBaseColorApi(TestBase):
  def test_get_base_color(self):
      response = self.client.get(url_for('get_base_color'))
      color = response.data.decode('utf-8')
      hex = color.split('#')[1]
      assert color[0] == '#'
      assert hex.isalnum() == True
      assert len(hex) == 6


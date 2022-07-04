from application_3 import app
from flask import url_for
from flask_testing import TestCase

class TestBase(TestCase):
  def create_app(self):
      return app

class TestPaletteTypeApi(TestBase):
  def test_get_palette_type(self):
      response = self.client.get(url_for('get_palette_type'))
      palette_type = response.data.decode('utf-8')
      assert palette_type in ['monochromatic', 'complementary', 'analogous', 'split-complementary']


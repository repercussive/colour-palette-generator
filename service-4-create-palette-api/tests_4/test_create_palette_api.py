from application_4 import app
from flask import url_for
from flask_testing import TestCase

class TestBase(TestCase):
  def create_app(self):
    return app

class TestCreatePaletteApi(TestBase):
  def test_create_palette(self):
    response = self.client.post(
        url_for('create_palette'),
        json=dict(base_color='#0000ff', palette_type='monochromatic')
    )
    colors = response.json['colors']
    assert type(colors) == list
    assert len(colors) >= 3
    

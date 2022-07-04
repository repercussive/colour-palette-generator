from application_1 import app
from flask import url_for
from flask_testing import TestCase
import requests_mock

class TestBase(TestCase):
  def create_app(self):
    return app

class TestFront(TestBase):
  def test_front(self):
    with requests_mock.Mocker() as mock:
      colors = ['#000075', '#0000c1', '#0f0fff', '#5b5bff', '#a8a8ff']
      mock.get('http://service-2:5000/get_base_color', text='#0f0fff')
      mock.get('http://service-3:5000/get_palette_type', text='monochromatic')
      mock.post(
        'http://service-4:5000/create_palette',
        json=dict(colors=colors)
      )
      response_data = self.client.get(url_for('index')).data.decode('utf-8')
      
      assert 'monochromatic' in response_data
      for color in colors: 
        assert color in response_data


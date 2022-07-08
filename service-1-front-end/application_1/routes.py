from application_1 import app
from flask import render_template
from colour import Color
import requests

@app.route('/')
def index():
  base_color = requests.get('http://service-2:5000/get_base_color').text
  palette_type = requests.get('http://service-3:5000/get_palette_type').text
  palette = requests.post(
      'http://service-4:5000/create_palette',
      json=dict(base_color=base_color, palette_type=palette_type)
  ).json()

  return render_template(
      'home.html',
      base_color=base_color,
      palette_type=palette_type,
      colors=[Color(color) for color in palette['colors']]
  )

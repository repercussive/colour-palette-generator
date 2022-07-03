from application import app
from random import random
from colour import Color

@app.route('/get_base_color')
def get_base_color():
  color = Color(
      hue=random(),
      saturation=0.8,
      luminance=0.5
  )
  return str(color)
from application import app
from random import choice

palette_types = ['monochromatic', 'complementary', 'analogous', 'split-complementary']

@app.route('/get_palette_type')
def get_palette_type():
  return choice(palette_types)
from application import app
from flask import request
from colour import Color

@app.route('/create_palette', methods=['POST'])
def create_palette():
  request_data = request.get_json()
  base_color = request_data['base_color'] # type: ignore
  palette_type = request_data['palette_type'] # type: ignore

  colors = []
  for offset in palette_offsets[palette_type]:
    color = Color(base_color)
    color.set_hue(color.get_hue() + (offset.get('h') or 0))
    color.set_saturation(clamp(color.get_saturation() + (offset.get('s') or 0), 0, 1))
    color.set_luminance(clamp(color.get_luminance() + (offset.get('l') or 0), 0, 0.9))
    colors.append(str(color))

  return dict(colors=colors)

def clamp(num, min_value, max_value):
  return max(min(num, max_value), min_value)

palette_offsets = {
  'monochromatic': [
    { 'l': -0.3 },
    { 'l': -0.15 },
    { 'l': 0 },
    { 'l': 0.15 },
    { 'l': 0.3 }
  ],
  'analogous': [
    { 'h': -0.1 },
    { 'h': -0.05 },
    { 'h': 0 },
    { 'h': 0.05 },
    { 'h': 0.1 }
  ],
  'complementary': [
    { 'h': 0, 'l': -0.2 },
    { 'h': 0, 's': -0.1 },
    { 'h': 0, 's': -0.1, 'l': 0.2 },
    { 'h': 0.5 },
    { 'h': 0.5, 's': -0.1, 'l': -0.15 }
  ],
  'split-complementary': [
    { 'h': -0.575, 'l': -0.075 },
    { 'h': -0.575 },
    { 'h': 0 },
    { 'h': 0.575 },
    { 'h': 0.575, 'l': -0.075 }
  ]
} 
from application import app
from flask import render_template
import requests

@app.route('/')
def index():
    base_color = requests.get('http://service-2:5000/get_base_color').text
    return render_template('home.html', base_color=base_color) 
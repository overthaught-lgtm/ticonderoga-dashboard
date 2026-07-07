import os
from flask import Flask, render_template

# This tells Flask exactly where to find the templates folder relative to Vercel's environment execution path
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def index():
    return render_template('index.html')

# DO NOT include app.run() here for Vercel production environments

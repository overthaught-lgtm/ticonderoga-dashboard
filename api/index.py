from flask import Flask, render_template

# 1. Must be named exactly 'app' (lowercase)
app = Flask(__name__, template_folder='../templates') 

@app.route('/')
def home():
    # 2. Make sure it points to your index.html file
    return render_template('index.html') 

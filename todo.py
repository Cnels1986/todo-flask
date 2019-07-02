from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "This will be the homepage of this app"

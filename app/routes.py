from app import app
from flask import render_template


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Amir"}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day!'
        },
        {
            'author': {'username': 'Doe'},
            'body': 'This book was a great read!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
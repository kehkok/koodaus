"""
    Get Started with Simple Flask Application

    Prerequisite:
    pip install flask

    To execute at command prompt:
    Option 1:
    Type: "python simple_flask.py"

    Option 2:
    - "export FLASK_APP=simple_flask.py"
    - "python -m flask run"

    Option 3:
    - "export FLASK_APP=simple_flask.py"
    - flask run --host=0.0.0.0
"""

import os
from flask import Flask, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome to Simple Flask Hello World! OR Type: " + \
            "http://localhost:5100:/google"


@app.route('/google')
def go_url_google():
    return redirect('http://www.google.com.my')


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5100))
    app.run(host='0.0.0.0', port=port)


#!/usr/bin/python3
""" This script starts the flask app and listern on 0.0.0.0:5000
    on / route
"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Returns some text. """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Returns hbnb """
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """ replace text with variable. """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

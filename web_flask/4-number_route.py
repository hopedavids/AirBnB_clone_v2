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


@app.route('/python/')
@app.route('/python/<text>')
def python_text(text='is cool'):
    """ replace more text with another variable. """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>')
def number_text(n):
    """ replace with int only if given an integer. """
    n = str(n)
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def html_num(n):
    """ display html if n is int. """
    n = str(n)
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

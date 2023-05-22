#!/usr/bin/python3
from flask import Flask

""" This script starts the flask app and listern on 0.0.0.0:5000
    on / route
"""

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!\n"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

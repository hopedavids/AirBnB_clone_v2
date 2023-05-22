#!/usr/bin/python3
"""this script starts flask application on 0.0.0.0 and port 5000  """


from flask import Flask, render_template
from models import storage


app = Flask(__name__)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

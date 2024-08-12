#!/usr/bin/python3
""" this module statr a web Application """
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ this method say!!! HBNB! """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def return_hbnb():
    """ this module say!! hbnb """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def about_c(text):
    """ this module says something about C """
    formated_text = text.replace('_', ' ')
    return f"C {formated_text}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>/', strict_slashes=False)
def route_python(text):
    """ this method say something about python """
    txt_fmrt = text.replace('_', ' ')
    return f"Python {txt_fmrt}"


@app.route('/number/<int:n>', strict_slashes=False)
def route_numbet(n):
    """ this method display number """
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

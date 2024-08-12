#!/usr/bin/python3
""" this module statr a web Application """
from flask import Flask, render_template


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


@app.route('/number_template/<int:n>', strict_slashes=False)
def render_teplate(n):
    """ this methos render a template """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def template_odd_even(n):
    """ this method templated an odded and evened """
    odd_even = "even" if n % 2 == 0 else "odd"
    return\
        render_template('6-number_odd_or_even.html', n=n, odd_even=odd_even)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

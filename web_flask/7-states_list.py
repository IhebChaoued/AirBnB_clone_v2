#!/usr/bin/python3
""" Flask web application """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ Hello """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ hbnb """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ c text """
    return 'c {}'.format(text.replace("_", " "))


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """ Python """
    return 'Python {}'.format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ num """
    return '{} is a number'.format(n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """ odd or even """
    if n % 2 == 0:
        p = 'even'
    else:
        p = 'odd'
    return render_template('6-number_odd_or_even.html', number=n, parity=p)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ states """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close(error):
    """ close """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

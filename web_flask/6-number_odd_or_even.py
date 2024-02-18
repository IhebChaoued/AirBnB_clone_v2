#!/usr/bin/python3
""" Flask App with Dynamic Routes and HTML Rendering """
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def greet():
    """ Route for the main index """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """ Route for the '/hbnb' endpoint """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_text(text):
    """ Route for the '/c/<text>' endpoint """
    text = text.replace("_", " ")
    return "C " + f"{text}"


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_framework(text):
    """ Route for the '/python' and '/python/<text>' endpoints """
    return 'Python {}'.format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def display_number(n):
    """ Route for the '/number/<int:n>' endpoint """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def display_number_template(n):
    """ Route for the '/number_template/<int:n>' endpoint """
    return render_template('5-number.html', number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def display_number_odd_or_even(n):
    """ Route for the '/number_odd_or_even/<int:n>' endpoint """
    if n % 2 == 0:
        p = "even"
    else:
        p = "odd"
    return render_template('6-number_odd_or_even.html', number=n, x=p)


if __name__ == "__main__":
    # Run the Flask app on specified host and port
    app.run(host="0.0.0.0", port=5000)

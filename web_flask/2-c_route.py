#!/usr/bin/python3
""" Flask App with Dynamic Route """
from flask import Flask

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


if __name__ == "__main__":
    # Run the Flask app on specified host and port
    app.run(host="0.0.0.0", port=5000)

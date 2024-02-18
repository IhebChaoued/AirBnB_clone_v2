#!/usr/bin/python3
""" Flask App with Multiple Routes """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """ Route for the main index """
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def indextwo():
    """ Route for the '/hbnb' endpoint """
    return "HBNB"


if __name__ == "__main__":
    # Run the Flask app on specified host and port
    app.run(host="0.0.0.0", port=5000)

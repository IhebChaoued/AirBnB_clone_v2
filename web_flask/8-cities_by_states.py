#!/usr/bin/python3
""" Flask App for Cities by States """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_storage(error):
    """ Teardown function to close the database connection """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def list_cities_by_states():
    """ Route to list cities and states """
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

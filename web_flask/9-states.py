#!/usr/bin/python3
"""Flask application for handling states"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """Displays states or specific state by ID"""
    not_found = False

    if id is not None:
        states = storage.all(State, id)
        with_id = True
        if len(states) == 0:
            not_found = True
    else:
        states = storage.all(State)
        with_id = False

    return render_template('9-states.html', states=states,
                           with_id=with_id, not_found=not_found)


@app.teardown_appcontext
def teardown(exception):
    """Closes storage"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

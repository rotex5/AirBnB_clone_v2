#!/usr/bin/python3
""" Flaskweb application for HBNB project """

from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close_db_conn(exception):
    """teardown session connection to db"""
    storage.close()


@app.route('/states', strict_slashes=False)
def list_states():
    """ passes a list state
    to /states route"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state_detail(id):
    """ passes a details of a state
    to /states/id route"""
    for state in storage.all(State).values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

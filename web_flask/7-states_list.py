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


@app.route('/states_list', strict_slashes=False)
def list_states():
    """ passes a list of states to /states_list route"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

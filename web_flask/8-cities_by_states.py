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


@app.route('/cities_by_states', strict_slashes=False)
def list_states():
    """ passes a list of cities by state
    to /cities_by_states route"""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

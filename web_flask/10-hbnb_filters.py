#!/usr/bin/python3
""" Flaskweb application for HBNB project """

from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.teardown_appcontext
def close_db_conn(exception):
    """teardown session connection to db"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """ passes queryset to /hbnb_filters route"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template("10-hbnb_filters.html",
                            states=states,
                            amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

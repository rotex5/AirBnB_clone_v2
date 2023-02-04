#!/usr/bin/python3
""" Flaskweb application for HBNB project """

from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place


app = Flask(__name__)


@app.teardown_appcontext
def close_db_conn(exception):
    """teardown session connection to db"""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ passes queryset to /hbnb route"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    return render_template("100-hbnb.html",
                            states=states,
                            amenities=amenities,
                            places=places)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

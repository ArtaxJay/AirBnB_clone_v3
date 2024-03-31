#!/usr/bin/python3
"""
This module returns the status message for successful API calls.
"""

from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.city import City
from models.state import State

from models import storage
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def api_status():
    """Reurns the status message for the API calls."""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def num_objs():
    """Gets the numerical values of each obj by type."""
    class_obj = [User, City, Place, State, Amenity, Review]

    cl_names = ["amenities", "cities", "places", "reviews", "states", "users"]

    counted_objs = {}
    for i in range(len(class_obj)):
        counted_objs[cl_names[i]] = storage.count(class_obj[i])

    return jsonify(counted_objs)

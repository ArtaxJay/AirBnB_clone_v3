#!/usr/bin/python3
""" This module defines the status code for all the requests. """

from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status_msg():
    """ HTTP status message if API GET rewuest is successful. """
    return jsonify({"status": "OK"})

#!/usr/bin/python3
"""The status message for all API call is defined here in this module."""

from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status_msg():
    """
    Status message for a successful API GET request call.
    """
    return jsonify({"status": "OK"})

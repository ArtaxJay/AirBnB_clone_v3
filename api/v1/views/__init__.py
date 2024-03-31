#!/usr/bin/python3
"""
__init__ naming convention makes this file the package file for this dir.
"""

from flask import Blueprint
from api.v1.views.index import *

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

#!/usr/bin/python3
""" The API face of the Airbnb clone project. """

from models import storage
from api.v1.views import app_views
from os import environ
from flask import Flask

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_db(error):
    """ Invoke the close() method on storage. """
    storage.close()


if __name__ == "__main__":
    """ Do not run this script as a module. """
    port = environ.get('HBNB_API_PORT')
    host = environ.get('HBNB_API_HOST')
    if not port:
        port = '5000'
    if not host:
        host = '0.0.0.0'

    app.run(host=host, port=port, threaded=True)

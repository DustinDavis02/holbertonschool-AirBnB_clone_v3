#!/usr/bin/python3
<<<<<<< HEAD
"""appy appears"""
from flask import Flask, make_response
from models import storage
from api.v1.views import app_views
from os import getenv as env
=======
""" API entry point """

from os import getenv
from flask import Flask, jsonify, make_response
>>>>>>> master
from flask_cors import CORS
from api.v1.views import app_views
from models import storage

app = Flask(__name__)
app.register_blueprint(app_views)

cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown_storage(exception):
    """ Tear down method """
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """ 404 Error handler """
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = getenv("HBNB_API_PORT", 5000)
    app.run(host=host, port=port, threaded=True)

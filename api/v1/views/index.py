#!/usr/bin/python3
"""index to connect to API"""
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def hbnbStatus():
    """hbnbStatus"""
    return jsonify({"status": "OK"})

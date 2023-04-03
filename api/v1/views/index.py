#!/usr/bin/python3
"""Index module to create an API endpoint"""
from flask import jsonify
from api.v1.views import app_views
from models import storage

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Returns a JSON with the status of the API"""
    return jsonify({'status': 'OK'})

@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """Returns a JSON with the number of objects in storage by type"""
    stats = {}
    for cls in storage.all().keys():
        stats[cls] = storage.count(cls)
    return jsonify(stats)

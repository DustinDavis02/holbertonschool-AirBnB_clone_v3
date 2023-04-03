#!/usr/bin/python3
from flask import jsonify
from api.v1.views import app_views
from models import storage

@app_views.route('/status')
def status():
    return jsonify({'status': 'OK'})

@app_views.route('/stats')
def stats():
    stats = {}
    for cls in storage.all().keys():
        stats[cls] = storage.count(cls)
    return jsonify(stats)

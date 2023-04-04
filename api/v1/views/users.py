#!/usr/bin/python3
"""Module for User objects that handles all default RESTFul API actions."""

from api.v1.views import app_views
from models import storage, User
from flask import jsonify, abort, request


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """Retrieves the list of all User objects"""
    users = storage.all(User).values()
    users_list = [user.to_dict() for user in users]
    return jsonify(users_list)
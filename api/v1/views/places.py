#!/usr/bin/python3
"""Defines the RESTful API actions for the Place object."""

from flask import jsonify, abort, request, make_response
from api.v1.views import app_views
from models import storage, Place, City, User
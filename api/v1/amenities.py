#!/usr/bin/python3
"""Amenities view module"""

from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.amenity import Amenity
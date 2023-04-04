#!/usr/bin/python3
"""State API routes"""

from api.v1.views import app_views
from models import storage
from models.state import State
from flask import jsonify, abort, request
#!/usr/bin/python3
"""This module contains the endpoint for the Review class."""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage
from models.review import Review
from models.place import Place
from models.user import User

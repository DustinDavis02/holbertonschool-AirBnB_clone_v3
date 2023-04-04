#!/usr/bin/python3
"""This module contains a route that retrieves all City objects"""
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.city import City
from models.state import State
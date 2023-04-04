#!/usr/bin/python3
"""Module for User objects that handles all default RESTFul API actions."""

from api.v1.views import app_views
from models import storage, User
from flask import jsonify, abort, request
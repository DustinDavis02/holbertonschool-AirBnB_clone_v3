#!/usr/bin/python3
"""Defines the RESTful API actions for the Place object."""

from flask import jsonify, abort, request, make_response
from api.v1.views import app_views
from models import storage, Place, City, User


@app_views.route('/cities/<city_id>/places', methods=['GET'], strict_slashes=False)
def get_places(city_id):
    """
    Retrieves the list of all Place objects of a City
    """
    city = storage.get(City, city_id)
    if city is None:
        abort(404)

    places_list = []
    places = city.places
    for place in places:
        places_list.append(place.to_dict())
    return jsonify(places_list)
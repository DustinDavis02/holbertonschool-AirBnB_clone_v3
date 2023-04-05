#!/usr/bin/python3
"""Defines the RESTful API actions for the Place object."""

from flask import jsonify, abort, request, make_response
from api.v1.views import app_views
from models import storage, Place, City, User


@app_views.route('/cities/<city_id>/places', methods=['GET'], strict_slashes=False)
def get_places(city_id):
    """Retrieves the list of all Place objects of a City"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)

    places_list = []
    places = city.places
    for place in places:
        places_list.append(place.to_dict())
    return jsonify(places_list)


@app_views.route('/places/<place_id>', methods=['GET'], strict_slashes=False)
def get_place(place_id):
    """Retrieves a Place object"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    return jsonify(place.to_dict())


@app_views.route('/places/<place_id>', methods=['DELETE'], strict_slashes=False)
def delete_place(place_id):
    """Deletes a Place object"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    storage.delete(place)
    storage.save()
    return jsonify({}), 200


@app_views.route('/cities/<city_id>/places', methods=['POST'], strict_slashes=False)
def create_place(city_id):
    """Creates a Place"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)

    request_data = request.get_json()
    if not request_data:
        return make_response(jsonify({"error": "Not a JSON"}), 400)

    user_id = request_data.get("user_id")
    if not user_id:
        return make_response(jsonify({"error": "Missing user_id"}), 400)
    user = storage.get(User, user_id)
    if user is None:
        abort(404)

    name = request_data.get("name")
    if not name:
        return make_response(jsonify({"error": "Missing name"}), 400)

    request_data['city_id'] = city_id
    new_place = Place(**request_data)
    storage.new(new_place)
    storage.save()

    return jsonify(new_place.to_dict()), 201


@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def update_place(place_id):
    """Updates a Place object"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)

    request_data = request.get_json()
    if not request_data:
        return make_response(jsonify({"error": "Not a JSON"}), 400)

    for key, value in request_data.items():
        if key not in ["id", "user_id", "city_id", "created_at", "updated_at"]:
            setattr(place, key, value)

    storage.save()

    return jsonify(place.to_dict()), 200

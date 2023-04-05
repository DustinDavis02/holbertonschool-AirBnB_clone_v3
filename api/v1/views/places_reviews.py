#!/usr/bin/python3
"""This module contains the endpoint for the Review class."""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage
from models.review import Review
from models.place import Place
from models.user import User


@app_views.route('/places/<place_id>/reviews', methods=['GET'])
def get_reviews(place_id):
    """Retrieves the list of all Review objects of a Place"""
    place = storage.get("Place", place_id)
    if place is None:
        abort(404)
    reviews_list = [review.to_dict() for review in place.reviews]
    return jsonify(reviews_list)


@app_views.route('/reviews/<review_id>', methods=['GET'])
def get_review(review_id):
    """Retrieves a Review object"""
    review = storage.get("Review", review_id)
    if review is None:
        abort(404)
    return jsonify(review.to_dict())


@app_views.route('/reviews/<review_id>', methods=['DELETE'])
def delete_review(review_id):
    """Deletes a Review object"""
    review = storage.get("Review", review_id)
    if review is None:
        abort(404)
    storage.delete(review)
    storage.save()
    return jsonify({}), 200


@app_views.route('/places/<place_id>/reviews', methods=['POST'])
def create_review(place_id):
    """Creates a Review object"""
    place = storage.get("Place", place_id)
    if place is None:
        abort(404)
    data = request.get_json()
    if data is None:
        return jsonify(error="Not a JSON"), 400
    if "user_id" not in data:
        return jsonify(error="Missing user_id"), 400
    user = storage.get("User", data["user_id"])
    if user is None:
        abort(404)
    if "text" not in data:
        return jsonify(error="Missing text"), 400
    review = Review(**data)
    review.place_id = place_id
    storage.new(review)
    storage.save()
    return jsonify(review.to_dict()), 201


@app_views.route('/reviews/<review_id>', methods=['PUT'])
def update_review(review_id):
    """Updates a Review object"""
    review = storage.get("Review", review_id)
    if review is None:
        abort(404)
    data = request.get_json()
    if data is None:
        return jsonify(error="Not a JSON"), 400
    ignore_keys = ["id", "user_id", "place_id", "created_at", "updated_at"]
    for key, value in data.items():
        if key not in ignore_keys:
            setattr(review, key, value)
    storage.save()
    return jsonify(review.to_dict()), 200
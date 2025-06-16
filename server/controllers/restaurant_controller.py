from flask import jsonify, request, make_response
from ..models import db
from ..models.restaurant import Restaurant



def get_all_restaurants():
    restaurants = [r.to_dict() for r in Restaurant.query.all()]
    
    if not restaurants:
        return make_response(jsonify({"error": "No restaurants found"}), 404)
    
    response = make_response(jsonify(restaurants), 200)
    return response


        
def get_by_id(restaurant_id):
    r = Restaurant.query.get(restaurant_id)
    
    if not r:
        return make_response(jsonify({"error": "Restaurant not found"}), 404)
    
    response = make_response(jsonify(r.to_dict()), 200)
    return response


def delete_restaurant(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)
    
    if not restaurant:
        return make_response(jsonify({ "error": "Restaurant not found" }), 404)
    
    db.session.delete(restaurant)
    db.session.commit()
    return '', 204


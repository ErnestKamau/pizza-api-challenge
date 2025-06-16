from flask import make_response, jsonify, request
from ..models import db
from ..models.restaurant_pizza import RestaurantPizza
from ..models.pizza import Pizza
from ..models.restaurant import Restaurant


def create_restaurant_pizza():
    data = request.get_json()
    
    try:
        new = RestaurantPizza(
            price=data["price"],
            restaurant_id=data["restaurant_id"],
            pizza_id=data["pizza_id"]
        )
        
        db.session.add(new)
        db.session.commit()
        
        r = new.to_dict()
        
        return make_response(r, 201)
    
    except Exception:
        db.session.rollback()
        return make_response(jsonify({ "errors": ["Price must be between 1 and 30"] }), 400)
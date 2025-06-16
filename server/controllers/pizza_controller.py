from flask import jsonify, request, make_response
from ..models import db
from ..models.pizza import Pizza


def all_pizzas():
    pizzas = [pizza.to_dict() for pizza in Pizza.query.all()]
    
    if not pizzas:
        return make_response(jsonify({"Error":"No restaurants found"}), 404)
    
    response = make_response(jsonify(pizzas), 200)
    return response


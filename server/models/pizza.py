from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
from . import db
from .restaurant_pizza import RestaurantPizza



class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'
    serialize_rules = ('-restaurant_pizzas.pizza',)
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    ingredients = db.Column(db.String, nullable=False)
    
    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='pizza')
    
    restaurants = association_proxy('restaurant_pizzas', "restaurant", creator=lambda restaurant_obj: RestaurantPizza(restaurant=restaurant_obj))
    
    def __repr__(self):
        return f"<Pizza {self.id}: {self.name}, Ingredients: {self.ingredients}>"
    


from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
from . import db
from .restaurant_pizza import RestaurantPizza


class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'
    serialize_rules = ('-restaurant_pizzas.restaurant',)
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    address = db.Column(db.String, nullable=False)
    
    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='restaurant', cascade='all, delete-orphan')
    
    pizzas = association_proxy('restaurant_pizzas', "pizza", creator=lambda pizza_obj: RestaurantPizza(pizza=pizza_obj))
    
    def __repr__(self):
        return f"<Restaurant {self.id}: {self.name}, {self.address}>"
    
    
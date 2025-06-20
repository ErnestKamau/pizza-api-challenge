from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from . import db



class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurant_pizzas'
    serialize_rules = ('-restaurant.restaurant_pizzas', '-pizza.restaurant_pizzas',)
    
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))
   
    restaurant = db.relationship('Restaurant', back_populates='restaurant_pizzas')
    pizza = db.relationship('Pizza', back_populates='restaurant_pizzas')
    
    
    @validates('price')
    def validate_price(self, key, price):
        if price < 1 or price > 30:
            raise ValueError("Price must be between 1 and 30.")
        return price
    
    def __repr__(self):
        return f"<id={self.id}, price={self.price}, restaurant_id={self.restaurant_id}, pizza_id={self.pizza_id}>"
    
   
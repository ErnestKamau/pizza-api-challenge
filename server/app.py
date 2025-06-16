from flask import Flask, request
from flask_migrate import Migrate
from .models import db
from .models.restaurant import Restaurant
from .models.pizza import Pizza
from .models.restaurant_pizza import RestaurantPizza
from .controllers.restaurant_controller import get_all_restaurants, get_by_id, delete_restaurant
from .controllers.pizza_controller import all_pizzas



app = Flask(__name__)
    
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza_restaurants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = True
    
db.init_app(app)
Migrate(app, db)

@app.route('/')
def index():
    body = {"message": "Welcome to pizza restaurants API"}
    return body


@app.route('/restaurants', methods=["Get"])
def get_restaurants():
    return get_all_restaurants()


@app.route('/restaurants/<int:restaurant_id>', methods=["GET"])
def get_restaurant(restaurant_id):
    return get_by_id(restaurant_id)


@app.route('/restaurant/<int:id>', methods=["DELETE"])
def del_restaurant(id):
    return delete_restaurant(id)


@app.route('/pizzas', methods=["GET"])
def get_all_pizzas():
    return all_pizzas()


    
    
    
if __name__ == '__main__':
    app.run(port=5555, debug=True)


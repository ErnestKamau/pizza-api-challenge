from flask import Flask, request
from flask_migrate import Migrate
from .models import db
from .models.restaurant import Restaurant
from .models.pizza import Pizza
from .models.restaurant_pizza import RestaurantPizza



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
    
    
if __name__ == '__main__':
    app.run(port=5555, debug=True)



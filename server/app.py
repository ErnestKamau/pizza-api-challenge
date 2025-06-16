from flask import Flask, request
from flask_migrate import Migrate
from .models import db



app = Flask(__name__)
    
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza_restaurants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = True
    
db.init_app(app)
Migrate(app, db)
    
    
if __name__ == '__main__':
    app.run(port=5555, debug=True)



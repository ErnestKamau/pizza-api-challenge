from server.app import app
from server.models import db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza


with app.app_context():
    print("Seeding database...")

    # Clear existing data
    RestaurantPizza.query.delete()
    Pizza.query.delete()
    Restaurant.query.delete()

    # Create restaurants
    r1 = Restaurant(name="Mama's Pizza", address="123 Main St")
    r2 = Restaurant(name="Pizza Palace", address="456 Side St")
    r3 = Restaurant(name="Neapolitan Express", address="789 Elm St")
    r4 = Restaurant(name="Joe's Pizza", address="592 Kingston St")
    r5 = Restaurant(name="GG's Italian Pizzeria", address="916 Pine Avenue")

    # Create pizzas
    p1 = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil")
    p2 = Pizza(name="Pepperoni", ingredients="Tomato, Mozzarella, Pepperoni")
    p3 = Pizza(name="Hawaiian", ingredients="Tomato, Mozzarella, Ham, Pineapple")

    # Add them to the session
    db.session.add_all([r1, r2, r3, r4, r5, p1, p2, p3])
    db.session.commit()

    # Create restaurant-pizza relationships with prices
    rp1 = RestaurantPizza(price=10, restaurant_id=r1.id, pizza_id=p1.id)
    rp2 = RestaurantPizza(price=12, restaurant_id=r1.id, pizza_id=p2.id)
    rp3 = RestaurantPizza(price=11, restaurant_id=r2.id, pizza_id=p2.id)
    rp4 = RestaurantPizza(price=14, restaurant_id=r2.id, pizza_id=p3.id)
    rp5 = RestaurantPizza(price=13, restaurant_id=r3.id, pizza_id=p1.id)
    rp6 = RestaurantPizza(price=20, restaurant_id=r5.id, pizza_id=p3.id)

    db.session.add_all([rp1, rp2, rp3, rp4, rp5, rp6])
    db.session.commit()

    print("Done seeding!")

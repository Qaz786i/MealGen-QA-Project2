from application import app, db
from application.models import Make_meal
import requests
from flask import render_template


@app.route('/')
def index():
    main_dish = requests.get('http://service_2:5000/get-mains')
    side_dish = requests.get('http://service_3:5000/##')
    price = requests.get('http:service_3:5000/##')
    db.session.add(Make_meal(main_dish=main_dish.json()["main_dish"], side_dish=side_dish.json()["side_dish"], price=price.json()["price"]))
    db.session.commit()
    meals = Make_meal.query.all() 
    return render_template('index.html', meals = meals)
from application import app, db
from application.models import Make_meal
import requests
from flask import render_template


@app.route('/')
def index():
    main_dish = requests.get('http://service_2:5000/get-mains')
    side_dish = requests.get('http://service_3:5000/get-side')
    price = requests.get('http://service_3:5000/post-meal')
    db.session.add(Make_meal(main=main.json()["main"], side=side.json()["side"], price_main=price_main.json()["price_main"], price_side=price_side.json()["price_side"], total_price=total_price.json()["total_price"]))
    db.session.commit()
    meals = Make_meal.query.all() 
    return render_template('index.html', meals = meals)



    ## look into how to add the pricing 
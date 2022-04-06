from application import app, db
from application.models import Make_meal
import requests
from flask import render_template, url_for


@app.route('/')
def index():
    main = requests.get('http://service_2:5000/get-mains')
    side = requests.get('http://service_3:5000/get-side')
    prices = requests.post('http://service_4:5000/post-meal', json={main=main.json()['main'], side=side.json()['side']})
    price_main = prices.json()['price_main']
    price_side = prices.json()['price_side']
    total_price = prices.json()['total_price']
    db.session.add(Make_meal(main=main.json()["main"], side=side.json()["side"], price_main=price_main, price_side=price_side, total_price=total_price))
    db.session.commit()
    meals = Make_meal.query.all()
    last5meals = Make_meal.query.order_by(Make_meal.id.desc()).limit(5).all() 
    return render_template('index.html', Make_meal = Make_meal, meals = meals, last5meals = last5meals)



@app.route('/history', methods=['GET'])
def history():
    meal_history = Make_meal.query.all
    return render_template("history.html", meal_history = meal_history) 

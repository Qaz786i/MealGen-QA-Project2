from application import app
from flask import request, jsonify

prices = {'Tuna Mayo Baguette':'3', 'Prawn Mayo Sandwich':'1', 'Chicken Tikka Curry and Biryani':'5', 'Ploughmans Cheese Sandwich':'2', 'Subway Footlong sub':'4', 'KFC Ricebox':'7', 'Prawn Cocktail Walkers':'1', 'Kettle Chips Sea Salt & Malt Vinegar':'2', 'Sensations Sweet Chili':'1', 'Fruit Bowl':'2', 'Pineapple Chunks':'2', 'Apple Slices':'1'}

@app.route('/post-meal', methods=['POST'])
def post_meal():
    main_json = request.get_json()
    main = main_json["main_dish"]
    side_json = request.json()
    side = side_json["side"]
    total_price = prices["main_dish"][main] + prices["main_dish"][side]
    return jsonify(price)



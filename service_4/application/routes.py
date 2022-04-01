from application import app
from flask import request, jsonify

prices = {'Tuna Mayo Baguette': 3, 'Prawn Mayo Sandwich': 1, 'Chicken Tikka Curry and Biryani': 5, 'Ploughmans Cheese Sandwich': 2, 'Subway Footlong sub': 4, 'KFC Ricebox': 7, 'Prawn Cocktail Walkers': 1, 'Kettle Chips Sea Salt & Malt Vinegar': 2, 'Sensations Sweet Chili': 1, 'Fruit Bowl': 2, 'Pineapple Chunks': 2, 'Apple Slices': 1}

@app.route('/post-meal', methods=['POST'])
def post_meal():
    data = request.get_json()
    mains = data_json["main"]
    sides = data_json["side"]
    price_main = prices[mains]
    price_side = prices[sides] 
    total_price = price_main + price_side
    return jsonify(price_main=price_main, price_side=price_side, total_price=total_price)
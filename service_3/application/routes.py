from application import app
from flask import jsonify, request
from random import choice

side = ['Prawn Cocktail Walkers', 'Kettle Chips Sea Salt & Malt Vinegar', 'Sensations Sweet Chili', 'Fruit Bowl', 'Pineapple Chunks', 'Apple Slices']

@app.route('/get-side', methods=['GET'])
def get_side():
    sides = choice(side)
    return jsonify(sides=sides)

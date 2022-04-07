from application import app
from flask import jsonify
from random import choice

sides = ['Prawn Cocktail Walkers', 'Kettle Chips Sea Salt & Malt Vinegar', 'Sensations Sweet Chili', 'Fruit Bowl', 'Pineapple Chunks', 'Apple Slices', 'Disco Salt and Vinegar', 'McCoys Thai Sweet Chicken']

@app.route('/get-side', methods=['GET'])
def get_side():
    side = choice(sides)
    return jsonify(side=side)

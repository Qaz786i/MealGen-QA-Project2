from application import app
from flask import jsonify
from random import choice

mains = ['Tuna Mayo Baguette', 'Prawn Mayo Sandwich', 'Chicken Tikka Curry and Biryani', 'Ploughmans Cheese Sandwich', 'Subway Footlong sub', 'KFC Ricebox']

@app.route('/get-mains', methods=['GET'])
def get_mains():
    main = choice(mains)
    return jsonify(main=main)

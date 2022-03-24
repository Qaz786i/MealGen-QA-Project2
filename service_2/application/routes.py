from application import app
from flask import jsonify
from random import choice

mains = ['Tuna Mayo Baguette', 'Prawn Mayo Sandwich', 'Chicken Tikka Curry and Biryani', 'Ploughmans Cheese Sandwich', 'Subway Footlong sub', 'KFC Ricebox', 'Jerk Chicken and Rice', 'Ceaser Chicken Salad', 'Falafel Wrap', 'Southern Fried Chicken Wrap', '!!!JACKPOT!!!Premium Wagyu Steak!!!JACKPOT!!', '!!!JACKPOT!!!Nandos Half Chicken!!!JACKPOT!!']

@app.route('/get-mains', methods=['GET'])
def get_mains():
    g_mains = choice(mains)
    return jsonify(mains=mains)

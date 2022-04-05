from application import db

class Make_meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    main_dish = db.Column(db.String(30), nullable=False)
    side_dish = db.Column(db.String(30), nullable=False)
    price_main = db.Column(db.Integer)
    price_side = db.Column(db.Integer)
    total_price = db.Column(db.Integer)
    def __str__(self):
        return f"Mains: {self.main_dish} {self.price_main}, Sides: {self.side_dish} {self.price_side}, Total Price: {self.price}"
from application import db

class Make_meal(db.Model):
    id = db.Column(db.Interger, primary_key=True)
    main_dish = db.Column(db.String(30), nullable=False)
    side_dish = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Integer)
    def __str__(self):
        return f"Mains: {self.main_dish}, Sides: {self.side_dish}, Total Price: {self.price}"
from models import db
from datetime import datetime

class Cart(db.Model):
    __tablename__ = "carts"
    cart_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, default=datetime.now)

    def serialize(self):
        return {
            "cart_id": self.cart_id,
            "user_id": self.user_id,
            "date": self.date
        }
    
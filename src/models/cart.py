from models import db
from datetime import datetime

class Cart(db.Model):
    __tablename__ = "carts"
    cart_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    date = db.Column(db.DateTime, default=datetime.now)
    product_ids = db.Column("product_ids", db.ARRAY(db.Integer), db.ForeignKey("products.product_id"))

    def serialize(self):
        return {
            "cart_id": self.cart_id,
            "user_id": self.user_id,
            "date": self.date,
            "product_ids": self.product_ids
        }

    def save(self):
        db.session.add()
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
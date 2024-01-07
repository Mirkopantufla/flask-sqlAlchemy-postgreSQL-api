from models import db

class Offer(db.Model):
    __tablename__= "offers"
    offer_id = db.Column(db.Integer(), primary_key=True)
    discount_type = db.Column(db.String(), nullable=False) # Puede ser % ó - (Así, puedo quitar un % del valor del producto, o restarle directamente cierta cantidad.)
    discount = db.Column(db.Integer(), nullable=False)
    image_id = db.Column(db.Integer(), nullable=False)
    product_id = db.Column(db.Integer(), nullable=False)

    def serialize(self):
        return {
            "offer_id": self.offer_id,
            "discount_type": self.discount_type,
            "discount": self.discount,
            "image_id": self.image_id,
            "product_id": self.product_id
        }


    def save(self):
        db.session.add(self)
        db.session.commit()

    def upload(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
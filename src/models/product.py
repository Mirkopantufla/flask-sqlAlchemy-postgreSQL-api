from models import db

class Product(db.Model):
    __tablename__ = "products"
    product_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    price = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(3000), nullable=False)
    category = db.Column(db.String(300))
    image_id = db.Column(db.Integer)
    rating = db.Column(db.String)

    def serialize(self):
        return {
            "product_id": self.product_id,
            "title": self.title,
            "price": self.price,
            "description": self.description,
            "category": self.category,
            "image_id": self.image_id,
            "rating": self.rating
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def upload(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
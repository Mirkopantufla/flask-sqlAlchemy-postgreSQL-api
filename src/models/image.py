from models import db

class Image(db.Model):
    __tablename__ = "images"
    image_id = db.Column(db.Integer, primary_key=True)
    image_src = db.Column(db.String(3000))
    cloud_public_id = db.Column(db.String(200))
    active = db.Column(db.Boolean, default=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'))

    # Serializo la imagen
    def serialize(self):
        return {
            "image_id": self.image_id,
            "image_src": self.image_src,
            "cloud_public_id": self.cloud_public_id,
            "active": self.active,
            "product_id": self.product_id
        }
        
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def update(self):
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
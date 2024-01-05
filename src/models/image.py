from models import db

class Image(db.Model):
    __tablename__ = "images"
    image_id = db.Column(db.Integer, primary_key=True)
    src_imagen = db.Column(db.String(3000))
    id_publico = db.Column(db.String(200))
    activo = db.Column(db.Boolean, default=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'))

    # Serializo la imagen
    def serialize(self):
        return {
            "image_id": self.image_id,
            "src_imagen": self.src_imagen,
            "id_publico": self.id_publico,
            "activo": self.activo,
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
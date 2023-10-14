from models import db

class ShipDetail(db.Model):
    __tablename__ = "ship_details"
    address_id = db.Column(db.Integer, primary_key=True)
    address_name = db.Column(db.String(300), nullable=False)
    address = db.Column(db.String(300), nullable=False)
    address_number = db.Column(db.Integer, nullable=False)
    aditional_info = db.Column(db.Integer)
    user_id = db.Column(db.Integer, nullable=False)
    commune_id = db.Column(db.Integer, nullable=False)
    region_id = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            "address_id": self.address_id,
            "address_name": self.address_name,
            "address": self.address,
            "address_number": self.address_number,
            "aditional_info": self.aditional_info,
            "user_id": self.user_id,
            "commune_id": self.commune_id,
            "region_id": self.region_id
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
from models import db

class Region(db.Model):
    __tablename__ = "regions"
    region_id = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(300), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    country_id = db.Column(db.Integer, nullable=False, default=0) #0 = Chile
    roman_number = db.Column(db.String(30), nullable=False)

    def serialize(self):
        return {
            "region_id": self.region_id,
            "name": self.name,
            "number": self.number,
            "country_id": self.country_id,
            "roman_number": self.roman_number
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
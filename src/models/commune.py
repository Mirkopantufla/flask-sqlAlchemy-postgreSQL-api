from models import db

class Comunne(db.Model):
    __tablename__ = "communes"
    commune_id = db.Column(db.String(100), primary_key=True)
    region_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            "commune_id": self.commune_id,
            "region_id": self.region_id,
            "name": self.name
        }
    
    def save(self):
        db.session.add()
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete()
        db.session.commit()
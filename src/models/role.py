from models import db
from sqlalchemy.orm import relationship

class Role(db.Model):
    __tablename__ = "roles"
    role_id = db.Column(db.Integer, primary_key=True) #0 Admin/1 Worker/2 Client
    description = db.Column(db.String(100), nullable=False)
    active = db.Column(db.Boolean, default=True)
    users = db.relationship("User", backref="roles")

    # Serializo el rol
    def serialize(self):
        return {
            "role_id": self.role_id,
            "description": self.description,
            "active": self.active
        }
    
    def serialize_with_users(self):
        return {
            "role_id": self.role_id,
            "description": self.description,
            "active": self.active,
            "users": self.get_users()
        }
    
    def get_users(self):
        return list(map(lambda user: user.serialize(), self.users))
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
from models import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    rut_numbers = db.Column(db.Integer, nullable=False, unique=True)
    first_name = db.Column(db.String(300), nullable=False)
    last_name = db.Column(db.String(300), nullable=False)
    phone_number = db.Column(db.BigInteger, nullable=False, unique=True) #Unico
    email = db.Column(db.String(300), nullable=False, unique=True) #Unico
    password = db.Column(db.String(300), nullable=False)
    terms_conditions = db.Column(db.Boolean, nullable=False, default=False)
    register_date = db.Column(db.DateTime, default=(datetime.now))
    role_id = db.Column(db.Integer, db.ForeignKey("roles.role_id"), default=2) #0 admin/1 worker/2 normalUser

    # Serializo el usuario
    def serialize(self):
        return {
            "user_id": self.user_id,
            "rut_numbers": self.rut_numbers,
            "first_name": self.first_name,
            "last_name": self.last_name, 
            "phone_number": self.phone_number,
            "email": self.email,
            "password": self.password,
            "terms_conditions": self.terms_conditions,
            "register_date": self.register_date,
            "role_id": self.role_id
        }
    
    def secure_serialize(self):
        return {
            "user_id": self.user_id,
            "rut_numbers": self.rut_numbers,
            "first_name": self.first_name,
            "last_name": self.last_name, 
            "phone_number": self.phone_number,
            "email": self.email,
            "terms_conditions": self.terms_conditions,
            "register_date": self.register_date,
            "role_id": self.role_id
        }
    
    def get_roles(self):
        return list(map(lambda role: role.serialize(), self.roles))
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

db = SQLAlchemy()

#admin user
class Admin(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    adminID = db.Column(db.String(20), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    dateOfReservation = db.Column(db.String(20), unique=True, nullable=False)
    payMetod = db.Column(db.String(20), unique=True, nullable=False)
    headCount = db.Column(db.Integer, unique=True, nullable=False)


    
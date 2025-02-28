from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

db = SQLAlchemy()

# class Clanok(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     nazov = db.Column(db.String(100), nullable=False)
#     obsah = db.Column(db.Text, nullable=False)

#     def __repr__(self):
#         return f'Článok: {self.nazov}'


class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    cat_name = db.Column(db.String(50))
    telephone = db.Column(db.String(15))
    email = db.Column(db.String(100))
    from_date = db.Column(db.Date)
    to_date = db.Column(db.Date)
    room = db.Column(db.String(50))
    
class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    AID = db.Column(db.String(150), unique=True, nullable=False)  # AdminID as plain text

    def check_password(self, admin_id):
        """Check if the provided admin_id matches the stored AdminID"""
        return self.AID == admin_id  # Direct comparison without hashing
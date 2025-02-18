# from flask_sqlalchemy import SQLAlchemy
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_login import UserMixin

# db = SQLAlchemy()

# class Clanok(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     nazov = db.Column(db.String(100), nullable=False)
#     obsah = db.Column(db.Text, nullable=False)

#     def __repr__(self):
#         return f'Článok: {self.nazov}'


# class User(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password_hash = db.Column(db.String(128), nullable=False)

#     def set_password(self, password):
#         self.password_hash = generate_password_hash(password)

#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)
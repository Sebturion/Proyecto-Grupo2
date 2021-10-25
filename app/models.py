# import models extensions
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin


# create an instance of the extension with initializing it
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(128), unique=True)
    password_enc = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean, default = False)


# Avion
class Plane(db.Model):
    __tablename__ = 'planes'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(64), unique=True)
    capacity = db.Column(db.Integer)
    state = db.Column(db.String(64))

class Destination(db.Model):
    __tablename__ = 'destinations'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True)
    description = db.Column(db.String)
    image = db.Column(db.String)

class Offer(db.Model):
    __tablename__ = 'offers'
    id = db.Column(db.Integer, primary_key=True)
    origin_offer = db.Column(db.Integer, db.ForeignKey('destinations.id'),
        nullable=False)
    destination_offer = db.Column(db.Integer, db.ForeignKey('destinations.id'),
        nullable=False)
    price = db.Column(db.Integer)


class Flight(db.Model):
    __tablename__ = 'flights'
    id = db.Column(db.Integer, primary_key=True)
    origin_offer = db.Column(db.Integer, db.ForeignKey('destinations.id'),
        nullable=False)
    destination_offer = db.Column(db.Integer, db.ForeignKey('destinations.id'),
        nullable=False)
    plane = db.Column(db.Integer, db.ForeignKey('planes.id'),
        nullable=False)
    state = db.Column(db.String(64))
    departure_time = db.Column(db.DateTime, nullable=True)
    arrival_time = db.Column(db.DateTime, nullable=True)
    pilot = db.Column(db.String(128))


    
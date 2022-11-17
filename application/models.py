from application import db
from datetime import date

# One subject can be assigned to many staff
class Users(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
   # Username = db.Column(db.String(30), nullable=True)
    phone_no = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    eventbookings = db.relationship('EventBookings', backref='eventbookingsbr')

class Events(db.Model):
    __tablename__ = 'events'
    event_id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(30), nullable=False)
    event_description = db.Column(db.String(60), nullable=False)
    event_date = db.Column(db.Date(), nullable=False)
    event_venue= db.Column(db.String(30), nullable=False)
    

class EventBookings(db.Model):
    __tablename__ = 'event_bookings'
    booking_id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.event_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    booking_date = db.Column(db.Date(), nullable=False)


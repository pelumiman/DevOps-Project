from flask_wtf import FlaskForm
from wtforms import  SubmitField, SelectField

class AddEventBooking(FlaskForm):
    Userlist = SelectField("User List", choices=[])
    Eventlist = SelectField("Event List", choices=[])
    submit = SubmitField("Submit")

class DeleteEventBooking(FlaskForm):
   event_id = SelectField("event id")
   submit = SubmitField("Submit")
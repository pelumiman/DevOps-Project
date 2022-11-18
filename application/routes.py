from application import app, db
from application.models import Users, Events, EventBookings
from application.forms import AddEventBooking, DeleteEventBooking
from flask import Flask, render_template, request, redirect, url_for

@app.route('/')
@app.route('/layout')
def layout():
     return render_template('layout.html')  
     
@app.route('/John')
def John():
     return render_template('John.html')  

@app.route('/Sarah')
def Sarah():
     return render_template('Sarah.html')  

@app.route('/View_Events', methods = ['GET', 'POST'])
def View_Events():
    pyevents = Events.query.all()
    pybookingsform = AddEventBooking()
    pybookingsform.Eventlist.choices = [(event.event_id, event.event_name) for event in Events.query.all()]
    pybookingsform.Userlist.choices = [(event.user_id, event.firstname) for event in Users.query.all()]
    if pybookingsform.validate_on_submit():
        if request.method == 'POST':
            addeventbooking = EventBookings(event_id=pybookingsform.Eventlist.data, 
            user_id=pybookingsform.Userlist.data,
            booking_date=Events.query.get(pybookingsform.Eventlist.data).event_date)
            db.session.add(addeventbooking)
            db.session.commit()
            return redirect(url_for('layout'))
    return render_template('View_Events.html', jievents=pyevents, jiform = pybookingsform )


@app.route('/View_J_Bookings', methods = ['GET', 'POST'])
def View_J_Bookings():
  deventbook = EventBookings.query.filter_by(user_id=1).all()
  dbookingsform = DeleteEventBooking()
  dbookingsform.event_id.choices = [(event.event_id,event.event_id) for event in deventbook]
  if dbookingsform.validate_on_submit():
        if request.method == 'POST':
            deleteeventbooking = EventBookings.query.get(dbookingsform.event_id.data)
            db.session.delete(deleteeventbooking)
            db.session.commit()
            return redirect(url_for('layout'))
  return render_template('View_J_Bookings.html',deventbook = deventbook, diform = dbookingsform)
   

@app.route('/View_S_Bookings', methods = ['GET', 'POST'])
def View_S_Bookings():
  sieventbook = EventBookings.query.filter_by(user_id=2).all()
  Sdbookingsform = DeleteEventBooking()
  Sdbookingsform.event_id.choices = [(event.event_id,event.event_id) for event in sieventbook]
  # if Sdbookingsform.validate_on_submit():
  if request.method == 'POST':
         deleteeventbooking = EventBookings.query.get(Sdbookingsform.event_id.data)
         db.session.delete(deleteeventbooking)
         db.session.commit()
         return redirect(url_for('layout'))
  return render_template('View_S_Bookings.html', sieventbook = sieventbook, sifrom = Sdbookingsform)

from application import db, app
from application.models import Users, Events, EventBookings
from datetime import date

#with app.app.context():
db.drop_all()
db.create_all()

data = [{"firstname": "John", "lastname": "cole", "phone_no":"0895467944", "email":"jcole@gmail.com" },
{"firstname": "sarah", "lastname": "paxton", "phone_no":"0872679844", "email":"spaxton@gmail.com"}]

data1 = [{"event_name": "Football wars", "event_description": "4 teams play knockout matches against each other until 1 comes out on top", "event_date":date(2022, 4,14), "event_venue":"Mulhuddart Arena" },
        {"event_name": "Paint battle", "event_description": "2 teams of 6 play a painnt ball match against each other", "event_date":date(2023, 9,20), "event_venue":"Fort Monty"},
        {"event_name": "Black Panther Premier", "event_description": "Red carper for Movie", "event_date":date(2023, 8,12), "event_venue":"Dublin city centre"},
        {"event_name": "Elcetric Festival", "event_description": "festival with many artists", "event_date":date(2023, 2,27), "event_venue":"Bristol city"}]

data2= [{"event_id": "1", "user_id": "1", "booking_date":date(2022, 4,14)},
        {"event_id": "2", "user_id": "2", "booking_date":date(2022, 6,20)}]

for i in data:
        user = Users(firstname=i["firstname"], lastname = i["lastname"], phone_no = i["phone_no"],email = i["email"])
        db.session.add(user)
        db.session.commit()

for l in data1:
        event = Events(event_name=l["event_name"], event_description = l["event_description"], event_date = l["event_date"],event_venue = l["event_venue"])
        db.session.add(event)
        db.session.commit()


for l in data2:
        eventbooking = EventBookings( event_id = l["event_id"], user_id = l["user_id"],booking_date = l["booking_date"])
        db.session.add(eventbooking)
        db.session.commit()
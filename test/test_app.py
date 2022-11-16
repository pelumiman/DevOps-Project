from flask_testing import TestCase
from application import app, db
from application.models import Users, Events, EventBookings 
from selenium import webdriver
from flask import url_for
from datetime import date

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
            )
        return app

    def setUp(self):
        #will be called before every test
        #create table chema
        db.create_all()
    
        data = [{"firstname": "John", "lastname": "cole", "phone_no":"0895467944", "email":"jcole@gmail.com" },
        {"firstname": "sarah", "lastname": "paxton", "phone_no":"0872679844", "email":"spaxton@gmail.com"}]
        for i in data:
            user = Users(firstname=i["firstname"], lastname = i["lastname"], phone_no = i["phone_no"],email = i["email"])
            db.session.add(user)
            db.session.commit()
        data1 = [{"event_name": "Football wars", "event_description": "4 teams play knockout matches against each other until 1 comes out on top", "event_date":date(2022, 4,14), "event_venue":"Mulhuddart Arena" },
        {"event_name": "Paint battle", "event_description": "2 teams of 6 play a painnt ball match against each other", "event_date":date(2023, 9,20), "event_venue":"Fort Monty"}]
        for l in data1:
            event = Events(event_name=l["event_name"], event_description = l["event_description"], event_date = l["event_date"],event_venue = l["event_venue"])
            db.session.add(event)
            db.session.commit()

        data2= [{"event_id": "1", "user_id": "1", "booking_date":date(2022, 4,14)},
        {"event_id": "2", "user_id": "2", "booking_date":date(2022, 6,20)}]
        for l in data2:
            eventbooking = EventBookings( event_id = l["event_id"], user_id = l["user_id"],booking_date = l["booking_date"])
            db.session.add(eventbooking)
            db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

#test layout page
class LayoutPage(TestBase):
    def test_layout_get(self):
        response =self.client.get(url_for('layout'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to Event Management", response.data)

class JohnPage(TestBase):
    def test_john_get(self):
        response =self.client.get(url_for('John'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome back John", response.data)

class SarahPage(TestBase):
    def test_sarah_get(self):
        response =self.client.get(url_for('Sarah'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome back Sarah", response.data)

class Sarah_B_Page(TestBase):
    def test_sarah_b_get(self):
        response =self.client.get(url_for('View_S_Bookings'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Your Event Bookings", response.data)

class Sarah_B_P_Page(TestBase):
    def test_sarah_b_get(self):
        response =self.client.post(url_for('View_S_Bookings'),
        follow_redirects = True, data = dict(event_id = 1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to Event Management", response.data)

class John_B_Page(TestBase):
    def test_john_b_get(self):
        response =self.client.get(url_for('View_J_Bookings'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Your Event Bookings", response.data)

class John_B_P_Page(TestBase):
    def test_john_b_get(self):
        response =self.client.post(url_for('View_J_Bookings'),
        follow_redirects = True, data = dict(event_id = 1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to Event Management", response.data)

class View_E_Page(TestBase):
    def test_view_get(self):
        response =self.client.get(url_for('View_Events'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"These are all availiable Events", response.data)

class View_E_P_Page(TestBase):
    def test_view_post(self):
        response =self.client.post(url_for('View_Events'),
        follow_redirects = True, data = dict(Userlist = 1, Eventlist = 1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to Event Management", response.data)
    
        

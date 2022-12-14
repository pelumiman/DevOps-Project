# DevOps-Project
This repository contains the contents of the Fundamental project

## Project Brief:
The objective of this project was to design and produce a web app for based around event Management. 
The app needed to have CRUD (create, read, update and delete) functionality. 
The Flask micro-framework used and the informationwas stored in a MySQL database comprised of a minimum of two tables sharing a one-to-many relationship.

<img width="305" alt="Screenshot 2022-11-14 195434" src="https://user-images.githubusercontent.com/65461503/202134138-5d71753c-2e73-4822-8972-331fa2d7b337.png">
The ERD for the MVP is displayed above.

## App Design:
The CRUD application I decided to create was an Event Management System.The application allows 2 specified users to View all upcoming Events, add those Events to their list of Event Bookings and they can also remove those events from their list of event bookings. Trello was very useful in laying out how to structure my project in a step by step process. Akanban template was used as seen here https://trello.com/b/hijDOIxa/kanban-template.

## Risk Assesment:
<img width="737" alt="image" src="https://user-images.githubusercontent.com/65461503/202199327-db0c3a10-fe18-4579-8e95-c71ad70ef5df.png">



## Testing:
The development environment used was a python3 virtual environment.The virtual environment(venv) allowed for alterations to be made without affecting any pip install that were already on the machine.

Unitesting:is a process in which small pieces of the code are tested to ensure proper functionality. 
This was done in my testing folder. All the tests passed to achieve an overall test coverage of 100%.
<img width="740" alt="Screenshot 2022-11-15 161956" src="https://user-images.githubusercontent.com/65461503/202155251-bd2ef7ef-1591-42bb-a680-74093f9ff71d.png">

The test.app.py tested all the routes to ensure they were all working.Some of the tests would ensure the route could successfully receive a response when required to and that the correct actions that were required would occur.


## The App:
1.Welcome page, Prompts you to choose user

<img width="543" alt="image" src="https://user-images.githubusercontent.com/65461503/202164452-e0ea49b2-258b-4d31-98ec-c54a07281856.png">

2.User John is chosen

<img width="422" alt="image" src="https://user-images.githubusercontent.com/65461503/202164578-f36c9f02-70cd-4605-a4f9-991b301d6f5f.png">

3.He has 2 options, check is Events Bookings or View all Events

<img width="784" alt="image" src="https://user-images.githubusercontent.com/65461503/202164912-20fb6c3e-6628-4984-bac0-35d29887bc06.png">

<img width="319" alt="image" src="https://user-images.githubusercontent.com/65461503/202164750-3380be00-6b21-429e-be2f-0912873a6782.png">

4.Football wars is added to User Johns Event Bookings, Once selected User is brought back to welcome page. He can now choose John and Check his Event Bookings

<img width="260" alt="image" src="https://user-images.githubusercontent.com/65461503/202165413-be0e5302-a6db-4c0f-a2ef-62dd8268d577.png">

5. On Johns Event bookings list, he has the option to delete Event, if he does so, Event is removed from list

<img width="303" alt="image" src="https://user-images.githubusercontent.com/65461503/202165709-118a8a54-1c86-4c9f-a3ea-2f5c774eab8e.png">

6.The same actions can be performed for Sarah

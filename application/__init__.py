from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# app definition
app = Flask(__name__)

# config stuff
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '123456789abcdefghijklmonp'


# create db class
db = SQLAlchemy(app)

from application import routes
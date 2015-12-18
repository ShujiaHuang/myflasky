from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)

from app import views

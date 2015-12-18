from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment

app = Flask(__name__)
app.config.from_object('config')

bootstrap = Bootstrap(app)
moment = Moment(app)

from app import views

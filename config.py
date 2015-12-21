import os

basedir = os.path.abspath(os.path.dirname(__file__))

# avoid 'Must provide secret_key to use csrf.'
CSRF_ENDBLED = True
SECRET_KEY = 'you-will-never-guess'

# SQLite database
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

MAIL_SERVER = 'smtp.mxhichina.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
FLASKY_MAIL_SUBJECT_PREFIX = '[My Flasky]'
FLASKY_MAIL_SENDER = 'My Flasky admin <info@gracegene.com>'
FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

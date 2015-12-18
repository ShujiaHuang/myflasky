import os

basedir = os.path.abspath(os.path.dirname(__file__))

# avoid 'Must provide secret_key to use csrf.'
CSRF_ENDBLED = True
SECRET_KEY = 'you-will-never-guess'

# SQLite database
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

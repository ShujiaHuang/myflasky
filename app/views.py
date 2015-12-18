"""
Name: Shujia Huang
Date: 2015-12-17
"""
from flask import render_template
from datetime import datetime

from app import app
from .forms import NameForm

@app.route('/', methods = ['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', 
                           form = form,
                           name = name,
                           current_time = datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name = name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

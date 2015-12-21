"""
Name: Shujia Huang
Date: 2015-12-17
"""
from flask import render_template, session, redirect, url_for, flash
from datetime import datetime

from app import app, db
from .forms import NameForm
from .models import User

@app.route('/', methods = ['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have change your name!')

        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
        else:
            session['known'] = True

        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', 
                           form = form,
                           name = session.get('name'),
                           known = session.get('known', False),
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

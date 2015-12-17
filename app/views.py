"""
Name: Shujia Huang
Date: 2015-12-17
"""
from flask import render_template

from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name = name)

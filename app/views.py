from app import app

@app.route('/')
@app.route('/index')
def index():
    return '<h1>Hello world</h1>' 

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s</h1>' % name

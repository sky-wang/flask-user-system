from flask import Flask
from flask import  render_template
from flask import g
import sqlite3
app = Flask(__name__)

# sql operations
DATABASE = '/db/database.db'

def connect_db():
    return sqlite3.connect(DATABASE)

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/loginout')
def loginout():
    pass
@app.route('/info')
def userinfo():
    pass
@app.route('/edit')
def editinfo():
    pass
if __name__ == '__main__':
    app.run(debug=True)

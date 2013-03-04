from flask import Flask
from flask import  render_template
app = Flask(__name__)

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

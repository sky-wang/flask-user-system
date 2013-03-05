#encoding=utf8
from flask import Flask
from flask import  render_template , request , redirect , url_for ,flash
from flask import g
from flask.ext import sqlalchemy
from flask import Config
from config import DATABASE ,SECRET_KEY
import re
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SECRET_KEY'] = SECRET_KEY

# database
db = sqlalchemy.SQLAlchemy(app)

class user(db.Model):
    UID = db.Column(db.Integer , primary_key=True,autoincrement=True) #id
    Username = db.Column(db.String , nullable=False,unique=True)
    Password = db.Column(db.String , nullable=False)
    Email = db.Column(db.String ,nullable = False)
    School = db.Column(db.String , nullable = True)
    Age = db.Column(db.Integer)
    Blog = db.Column(db.String)
    Introduction = db.Column(db.String)

    def __init__(self , username , password , email , school = 'none' , age = 0 , blog='http://baidu.com',introdution='please introduce youself!'):
        self.Username = username
        self.Password = password
        self.Email = email
        self.School = school
        self.Age = age
        self.Blog = blog
        self.Introduction =introdution
    def __repr__(self):
        return '<User %s>'%self.Username

def vali(newone):
    if user.query.filter_by(Username=newone.Username).count() > 0:
        return 0
    if len(newone.Password) < 6:
        return 0
    return 1
# views
@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/reg',methods=['GET','POST'])
def reg():
    if request.method == 'GET':
        return render_template('reg.html')
    else:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        age = request.form['age']
        school = request.form['school']
        blog = request.form['blog']
        intro = request.form['intro']
        newuser = user(username , password , email , age , school , blog , intro)
        if vali(newuser):
            db.session.add(newuser)
            db.session.commit()
            redirect(url_for(userinfo))
        else :
            render_template('tip.html',msg='注册信息不合法！')
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

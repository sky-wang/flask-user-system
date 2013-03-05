# -*- coding: utf-8 -*-
from flask import Flask
from flask import  render_template , request , redirect , url_for ,flash , session
from flask.ext import sqlalchemy
from config import DATABASE ,SECRET_KEY
import re
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SECRET_KEY'] = SECRET_KEY

# database
db = sqlalchemy.SQLAlchemy(app)

class user(db.Model):
    UID = db.Column(db.Integer , primary_key=True,autoincrement=True,unique=True) #id
    Username = db.Column(db.String , nullable=False,)
    Password = db.Column(db.String , nullable=False)
    Email = db.Column(db.String ,nullable = False)
    School = db.Column(db.String , nullable = True)
    Age = db.Column(db.Integer)
    Blog = db.Column(db.String)
    Introduction = db.Column(db.String)

    def __init__(self , username , password , email , school = 'none' , age = 0 , blog='http://baidu.com',introdution='i am too lazy~~'):
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
        print "get"
        return render_template('reg.html')
    else:
        print "post"
        username = request.form['username']
        password = request.form['password']
        repassword = request.form['repassword']
        email = request.form['email']

        print "< %s %s %s>" % (username , password ,email)
        if password != repassword:
            flash("passwords doesn't match!!")
            return render_template('reg.html')

        newuser = user(username , password , email )
        print newuser
        if vali(newuser):
            db.session.add(newuser)
            db.session.commit()
            flash("Registration is successful!")
            return redirect(url_for('info'))
        else :
            flash("Registration is not successful!")
            return redirect(url_for('login'))

@app.route('/login' , methods=['GET','POST'])
def login():
    if 'username' in session:
        flash("Already logged in, please exit!")
        redirect(url_for('info'))
    else :
        if request.method == 'GET':
            return render_template('login.html')
        else :
            email = request.form['email']
            password = request.form['password']
            User = user.query.filter_by(Email = email , Password = password).first()
            if User is None:
                flash("email or password is wrong!!")
                return render_template('login.html')
            else:
                session['username'] = User.Username
                session['email'] = User.Email
                flash("login successful!")
                return render_template('info.html',user = User)

@app.route('/logout')
def logout():
    if 'username' in session:
        session.clear()
        return render_template('sucexit.html')
    else:
        return render_template('nologin.html')

@app.route('/info')
def info():
    if 'username' in session:
        User = user.query.filter_by(Email = session['email']).first()
        return render_template('info.html',user =User)
    else :
        flash("Please login system first !!")
        return redirect(url_for('login'))


@app.route('/edit' , methods=['GET','POST'])
def editinfo():

    if 'username' in session:
        print 'have'
        User = user.query.filter_by(Email = session['email']).first_or_404()
        print 'hh'
        if request.method == 'POST':
            print "post"
            username = request.form['username']
            email = User.Email;
            password = User.Password
            school = request.form['school']
            blog = request.form['blog']
            intro = request.form['intro']
            age =int( request.form['age'] )
            user.query.filter_by(Email = email).update(     dict(Username = username,
                                                            Password = password,
                                                            Email = email,
                                                            School=school,
                                                            Blog=blog,
                                                            Age=age,
                                                            Introdution=intro))
            db.session.commit()
            return redirect(url_for('info'))
        else :
            return render_template('edit.html',user =User)
    else :
        flash("Please login system first !!")
        return redirect(url_for('login'))



if __name__ == '__main__':
    app.run(debug=True)

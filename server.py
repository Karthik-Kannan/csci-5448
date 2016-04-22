from flask import Flask, render_template , jsonify ,request, flash, redirect, url_for
from flask.ext.login import login_user , logout_user , current_user , login_required
from flask.ext.bootstrap import Bootstrap
from flask.ext.mongoalchemy import MongoAlchemy
from flask.ext.triangle import Triangle
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy

import datetime , random
from datetime import datetime



login_manager = LoginManager()

app = Flask(__name__)
app.secret_key = 'N0thInGiSImP0sSiBl3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/testr'

login_manager.init_app(app)
db = SQLAlchemy(app)
Triangle(app)
Bootstrap(app)

login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))




@app.route('/')
def welcome():
    return render_template('welcome.html')



@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/student',methods=['GET', 'POST'])
@login_required
def student():
    return render_template('student.html')



class User(db.Model):
    __tablename__ = "users"
    id = db.Column('user_id',db.Integer , primary_key=True)
    username = db.Column('username', db.String(20), unique=True , index=True)
    password = db.Column('password' , db.String(10))
    email = db.Column('email',db.String(50),unique=True , index=True)
    registered_on = db.Column('registered_on' , db.DateTime)

    def __init__(self , username ,password , email):
        self.username = username
        self.password = password
        self.email = email
        self.registered_on = datetime.utcnow()

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.username)


@app.route('/register' , methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    user = User(request.form['username'] , request.form['password'],request.form['email'])
    db.session.add(user)
    db.session.commit()
    flash('User successfully registered')
    return redirect(url_for('login'))


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form['username']
    password = request.form['password']
    registered_user = User.query.filter_by(username=username,password=password).first()
    print registered_user
    if registered_user is None:
        flash('Username or Password is invalid' , 'error')
        return redirect(url_for('login'))
    login_user(registered_user)
    flash('Logged in successfully')
    return redirect(request.args.get('index') or url_for('index'))


if __name__ == '__main__':
  app.debug = True
  app.run(debug=True)

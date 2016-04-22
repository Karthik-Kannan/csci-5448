from flask import Flask, render_template , jsonify ,request
from flask.ext.bootstrap import Bootstrap
from flask.ext.mongoalchemy import MongoAlchemy
from flask.ext.triangle import Triangle
import datetime

app = Flask(__name__)

app.config['MONGOALCHEMY_DATABASE'] = 'library'

db = MongoAlchemy(app)
Triangle(app)
Bootstrap(app)


@app.route('/',methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/student',methods=['GET', 'POST'])
def student():
    return render_template('student.html')




class User(db.Document):
    userName = db.StringField()
    password = db.StringField()
    role = db.StringField()
    profilePhoto = db.StringField()
    displayName = db.StringField()
    regsiteredOn = db.DateTimeField()

    def __init__(self , password , email):
        self.userName = email
        self.password = password
        self.regsiteredOn = datetime.utcnow()


if __name__ == '__main__':
  app.debug = True
  app.run(debug=True)

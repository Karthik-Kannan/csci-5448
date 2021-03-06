from flask import Flask, render_template , jsonify ,request, flash, redirect, url_for
from flask.ext.login import login_user , logout_user , current_user , login_required
# from flask.ext.wtf import Form
# from wtforms import TextField, TextAreaField, SubmitField
from flask.ext.bootstrap import Bootstrap
from flask.ext.mongoalchemy import MongoAlchemy
from flask.ext.triangle import Triangle
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug.datastructures import ImmutableMultiDict
from bson.objectid import ObjectId 
import json

import datetime , random
from datetime import datetime



import pymongo
from pymongo import MongoClient
client = MongoClient('localhost', 27017)

dbMongo = client['testr']
question = dbMongo['question']
test = dbMongo['test']
answer = dbMongo['answer']

login_manager = LoginManager()

app = Flask(__name__)
app.secret_key = 'N0thInGiSImP0sSiBl3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/testr'

login_manager.init_app(app)
db = SQLAlchemy(app)
Triangle(app)
Bootstrap(app)

login_manager.login_view = 'login'


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




@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))




@app.route('/')
def welcome():
    return render_template('welcome.html')



@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/setQuestion',methods=['GET', 'POST'])
def setQuestion():
    print "Hello"
    question = dict(request.form)
    # print request.form.getlist('question'), request.form.getlist('category'), request.form.getlist('maxMarks'),request.form.getlist('answerType'),request.form.getlist('referenceAnswer')

    dbMongo.question.insert_one({'question': question['question'][0],
                                 'category': question['category'][0],
                                 'maxMarks': question['maxMarks'][0] ,
                                 'answerType': question['answerType'][0] ,
                                 'referenceAnswer': question['referenceAnswer'][0] ,
                                 'options': question['options'][0]
                                 } );
    # dbMongo.question.insert({'test': 'test'})
    return render_template('index.html')
    #return 'Hello from Flask!'


@app.route('/setQuestions',methods=['GET', 'POST'])
def setQuestions():
    print "Hello"
    # questions = dict(request.form)
    questions = json.loads(request.data.decode())
    for question in questions:
        print question
        dbMongo.question.insert_one({'question': question['question'],
                                 'category': question['category'],
                                 'maxMarks': question['maxMarks'] ,
                                 'answerType': question['answerType'],
                                 'referenceAnswer': question['referenceAnswer'],
                                 'options': question['options']
                                 } );

    flash("Question Bank Updated")
    return 'Hello from Flask!'



@app.route('/setAnswers',methods=['GET', 'POST'])
def setAnswers():
    answers = json.loads(request.data.decode())
    testName = answers['testName']
    for question in answers['answers']:
        dbMongo.answer.insert_one({'testName': testName , 'questionID': question , 'answer': answers['answers'][question]})

    flash("Test submitted.")
    return "Hello from Flask!"



@app.route('/takeTest/', defaults={'testId': None })
@app.route('/takeTest/<testId>')
def takeTest(testId):
    testData = list(dbMongo.test.find({'_id': ObjectId(testId)}))
    for questionId in testData[0]['questions']:
        print questionId
        questionActual = list(dbMongo.question.find({'_id': ObjectId(questionId)}))
        testData.append(questionActual)

    print testData
    return render_template('takeTest.html',testData = testData)
    


@app.route('/setTest',methods=['GET', 'POST'])
def setTest():
    testInfo = json.loads(request.data.decode())
    dbMongo.test.insert_one(testInfo)
    print testInfo

    flash("Test Created")
    return 'Hello from Flask!'
          
                                 
@app.route('/createTests',methods=['GET', 'POST'])
def createTests():
    questions_list = list(dbMongo.question.find())
    print "ghost ", questions_list
    return render_template('tests.html', q_list = questions_list)

@app.route('/listTests',methods=['GET', 'POST'])
def listTests():
    test_list = list(dbMongo.test.find())
    return render_template('listTests.html', t_list = test_list)



@app.route('/student',methods=['GET', 'POST'])
@login_required
def student():
    return render_template('student.html')

@app.route('/teacher', methods=['GET', 'POSTS'])
@login_required
def teacher():
    print "Teacher"
    return render_template('teacher.html')


@app.route('/question',methods=['GET', 'POST'])
@login_required
def question():
    return render_template('question.html')



@app.route('/questions',methods=['GET', 'POST'])
@login_required
def questions():
    return render_template('questions.html')


@app.route('/viewGrades',methods=['GET', 'POST'])
@login_required
def viewGrades():
    return render_template('viewGrade.html')



@app.route('/register' , methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    if not str(request.form['email']).endswith("colorado.edu"):
        flash('Please register with @colorado.edu account')
        return redirect(url_for('register'))

    user = User(request.form['username'] , request.form['password'],request.form['email'])
    db.session.add(user)
    db.session.commit()
    flash('User successfully registered')
    return redirect(url_for('contact'))

# class Contact(Form):
#   firstname = TextField("First Name")
#   lastname = TextField("First Name")
#   university = TextField("University")
#   phone = TextField("Phone Number")
#   submit = SubmitField("Submit")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    #~ form = ContactForm() return render_template('contact')

    if request.method == 'POST':
        return render_template('login.html')
 
    if request.method == 'GET':
        return render_template('contact.html')

    # contact = Contact(request.form['firstname'],
    #                   request.form['lastname'],
    #                   request.form['university'],
    #                   request.form['phone'])

@app.route('/performanceAnalysis',methods=['GET','POST'])
def performanceAnalysis(chartID = 'chart_ID', chart_type = 'bar', chart_height = 350):
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
    series = [{"name": 'Label1', "data": [1,2,3]}, {"name": 'Label2', "data": [4, 5, 6]}]
    title = {"text": 'My Title'}
    xAxis = {"categories": ['xAxis Data1', 'xAxis Data2', 'xAxis Data3']}
    yAxis = {"title": {"text": 'yAxis Label'}}
    return render_template('performanceanalysis.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form['username']
    password = request.form['password']
    registered_user = User.query.filter_by(username=username,password=password).first()
    print registered_user.username
    if registered_user is None:
        flash('Username or Password is invalid' , 'error')
        return redirect(url_for('login'))
    elif registered_user.username =='teacher':
        login_user(registered_user)
        return redirect(request.args.get('teacher') or url_for('teacher'))

    login_user(registered_user)
    flash('Logged in successfully')
    return redirect(request.args.get('student') or url_for('student'))


if __name__ == '__main__':
  app.debug = True
  app.run(debug=True)

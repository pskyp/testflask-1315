import urllib

from PIL import Image
import pymysql.cursors
import FairyImage
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required, current_user, roles_accepted, roles_required
import os
import sys


sys.path.insert(1, os.path.join(os.path.abspath('.'), "virtenv/lib/python2.7/site-packages"))

CLOUDSQL_PROJECT = 'testflask-1315'
CLOUDSQL_INSTANCE = 'us-central:fairydb'



# Create app
app = Flask(__name__)
# Create database connection object



app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super-secret'
app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_POST_LOGIN_VIEW'] = '/home'
app.config['SECURITY_POST_REGISTER_VIEW'] = '/home'


if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:TestFlask@104.197.55.21/My_Fairy_Kingdom'
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://dbuser:TestFlask@127.0.0.1/my_fairy_kingdom'

db = SQLAlchemy(app)


# Define models
roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
# db.create_all()
# user_datastore.create_user(email='pierswilcox@gmail.com', password='pierswilcox')
# db.session.commit()
# user_datastore.create_role(name='admin',description='site admin role')
# user_datastore.create_role(name='basic',description='free user')
# user_datastore.create_role(name='premium',description='paid user')
role = user_datastore.find_role('admin')
user_datastore.add_role_to_user(user_datastore.find_user(email='pierswilcox@gmail.com'),role)
db.session.commit()

# Create a user to test with
# @app.before_first_request
# def create_user():
#     db.create_all()
#     user_datastore.create_user(email='pierswilcox@gmail.com', password='pierswilcox')
#     db.session.commit()



#views

@app.route('/')

def start():

    return render_template("start.html")



@app.route('/welcome')

def index():
    import StringIO
    fairy = FairyImage.getrandomfairy()
    imgstring = fairy['image']
    filelike = StringIO.StringIO(imgstring)
    canvas = Image.open(filelike)
    canvas = FairyImage.addFairyNametoImage(canvas, fairy)
    output=StringIO.StringIO()
    canvas.save(output, format="JPEG")
    contents= output.getvalue().encode('base64')
    output.close()

    return render_template("index.html",contents=urllib.quote(contents.rstrip('\n')))

@app.route('/login')

def login():
    import StringIO
    fairy = FairyImage.getrandomfairy()
    imgstring = fairy['image']
    filelike = StringIO.StringIO(imgstring)
    canvas = Image.open(filelike)
    canvas = FairyImage.addFairyNametoImage(canvas, fairy)
    output=StringIO.StringIO()
    canvas.save(output, format="JPEG")
    contents= output.getvalue().encode('base64')
    output.close()

    return render_template("index.html",contents=urllib.quote(contents.rstrip('\n')))


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500




@app.route('/home')
def home():
    import StringIO

    fairy = FairyImage.getrandomfairy()
    imgstring = fairy['image']
    filelike = StringIO.StringIO(imgstring)
    canvas = Image.open(filelike)
    canvas = FairyImage.addFairyNametoImage(canvas, fairy)
    output=StringIO.StringIO()
    canvas.save(output, format="JPEG")
    contents= output.getvalue().encode('base64')
    output.close()
    isadmin = current_user.has_role('admin')
    loggedin = current_user.is_authenticated
    return render_template("main.html",contents=urllib.quote(contents.rstrip('\n')),admin =isadmin, auth=loggedin)


@app.route('/montage8')
def montage8():
    # print 8 random fairies
    import StringIO
    size = 800, 550
    canvas = FairyImage.getrandomfairysheet(8)
    canvas.thumbnail(size, Image.ANTIALIAS)
    output = StringIO.StringIO()
    canvas.save(output, format="JPEG")
    contents = output.getvalue().encode('base64')
    output.close()
    isadmin = current_user.has_role('admin')
    loggedin = current_user.is_authenticated
    return render_template('montage.html', contents=urllib.quote(contents.rstrip('\n')),admin =isadmin, auth=loggedin)


@app.route('/montage12')
# print first 12 fairies
def montagea12():
    import StringIO
    size = 800, 550
    canvas = FairyImage.getfairysheet(12)
    canvas.thumbnail(size, Image.ANTIALIAS)
    output=StringIO.StringIO()
    canvas.save(output, format="JPEG")
    contents= output.getvalue().encode('base64')
    output.close()
    isadmin = current_user.has_role('admin')
    loggedin = current_user.is_authenticated
    return render_template('montage12.html', contents=urllib.quote(contents.rstrip('\n')),admin =isadmin, auth=loggedin)


@app.route('/montage100')
# print first 80 fairies
def montage100():
    import StringIO
    size = 1200, 4400
    canvas = FairyImage.getfairysheet(80)
    canvas.thumbnail(size, Image.ANTIALIAS)
    output = StringIO.StringIO()
    canvas.save(output, format="JPEG")
    contents = output.getvalue().encode('base64')
    output.close()
    isadmin = current_user.has_role('admin')
    loggedin = current_user.is_authenticated
    return render_template('montage100.html', contents=urllib.quote(contents.rstrip('\n')),admin =isadmin, auth=loggedin)

@app.route('/db')
@roles_accepted('admin')
def db():
    gfairies = FairyImage.numberoffairies('f')
    bfairies = FairyImage.numberoffairies('m')
    tfairies = bfairies+gfairies
    fairyref = FairyImage.getfairyreferences('FAIRY_TBL')
    loggedin = current_user.is_authenticated

    return render_template("dblist.html",gfairies=str(gfairies), bfairies=str(bfairies),tfairies=str(tfairies),fairyref=str(fairyref), auth=loggedin)


@app.route('/deletedbtbl')
@roles_accepted('admin')
def deletedb_TBL():
    FairyImage.delete_table('FAIRY_TBL')

    gfairies = FairyImage.numberoffairies('f')
    bfairies = FairyImage.numberoffairies('m')
    tfairies = bfairies + gfairies
    fairyref = FairyImage.getfairyreferences('FAIRY_TBL')
    loggedin = current_user.is_authenticated
    return render_template("dblist.html", gfairies=str(gfairies), bfairies=str(bfairies), tfairies=str(tfairies),
                           fairyref=str(fairyref), auth=loggedin)


@app.route('/createdbtbl')
@roles_accepted('admin')
def createdb_TBL():
    FairyImage.create_fairy_table('FAIRY_TBL')
    gfairies = FairyImage.numberoffairies('f')
    bfairies = FairyImage.numberoffairies('m')
    tfairies = bfairies + gfairies
    fairyref = FairyImage.getfairyreferences('FAIRY_TBL')
    loggedin = current_user.is_authenticated
    return render_template("dblist.html", gfairies=str(gfairies), bfairies=str(bfairies), tfairies=str(tfairies),
                           fairyref=str(fairyref), auth=loggedin)


@app.route('/resetdb')
@roles_accepted('admin')
def resetDB():
    FairyImage.resetDB(15)
    gfairies = FairyImage.numberoffairies('f')
    bfairies = FairyImage.numberoffairies('m')
    tfairies = bfairies + gfairies
    fairyref = FairyImage.getfairyreferences('FAIRY_TBL')
    loggedin = current_user.is_authenticated
    return render_template("dblist.html", gfairies=str(gfairies), bfairies=str(bfairies), tfairies=str(tfairies),
                           fairyref=str(fairyref), auth=loggedin)


@app.route('/addgfairy')
def addgfairy():
    import StringIO
    newfairy = FairyImage.createfairy('f')
    canvas = FairyImage.getfairypicfromdb(newfairy['name'])
    canvas = FairyImage.addFairyNametoImage(canvas, newfairy)
    output = StringIO.StringIO()
    canvas.save(output, format="JPEG")
    contents = output.getvalue().encode('base64')
    output.close()
    loggedin = current_user.is_authenticated
    gfairies = FairyImage.numberoffairies('f')
    bfairies = FairyImage.numberoffairies('m')
    tfairies = bfairies + gfairies
    fairyref = FairyImage.getfairyreferences('FAIRY_TBL')

    return render_template("dblist2.html", gfairies=str(gfairies), bfairies=str(bfairies), tfairies=str(tfairies),
                           fairyref=str(fairyref), contents=urllib.quote(contents.rstrip('\n')), auth=loggedin)


@app.route('/10newfairy')
def add10randomfairy():
    FairyImage.createrandomfairies(10)
    gfairies = FairyImage.numberoffairies('f')
    bfairies = FairyImage.numberoffairies('m')
    tfairies = bfairies + gfairies
    fairyref = FairyImage.getfairyreferences('FAIRY_TBL')
    loggedin = current_user.is_authenticated
    return render_template("dblist.html", gfairies=str(gfairies), bfairies=str(bfairies), tfairies=str(tfairies),
                           fairyref=str(fairyref), auth=loggedin)


@app.route('/addbfairy')
def addbfairy():
    import StringIO
    newfairy = FairyImage.createfairy('m')
    canvas = FairyImage.getfairypicfromdb(newfairy['name'])
    canvas = FairyImage.addFairyNametoImage(canvas, newfairy)
    output = StringIO.StringIO()
    canvas.save(output, format="JPEG")
    contents = output.getvalue().encode('base64')
    output.close()
    loggedin = current_user.is_authenticated
    gfairies = FairyImage.numberoffairies('f')
    bfairies = FairyImage.numberoffairies('m')
    tfairies = bfairies + gfairies
    fairyref = FairyImage.getfairyreferences('FAIRY_TBL')

    return render_template("dblist2.html", gfairies=str(gfairies), bfairies=str(bfairies), tfairies=str(tfairies),
                           fairyref=str(fairyref), contents=urllib.quote(contents.rstrip('\n')), auth=loggedin)


@app.route('/fcard')
def fairycardimage():
    import StringIO
    fairy = FairyImage.getrandomfairy()
    imgstring = fairy['image']
    filelike = StringIO.StringIO(imgstring)
    canvas = Image.open(filelike)
    # canvas = FairyImage.getfairypicfromdb(fairy['name'])
    canvas = FairyImage.addFairyNametoImage(canvas, fairy)
    canvas = FairyImage.addFairyChartoImage(canvas, fairy)
    output = StringIO.StringIO()
    canvas.save(output, format="JPEG")
    contents = output.getvalue().encode('base64')
    output.close()
    isadmin = current_user.has_role('admin')
    loggedin = current_user.is_authenticated
    return render_template("main.html", contents=urllib.quote(contents.rstrip('\n')),admin =isadmin, auth=loggedin)


@app.route('/fdetailcard')
def fairydetailcardimage():
    import StringIO
    fairy = FairyImage.getrandomfairy()
    imgstring = fairy['image']
    filelike = StringIO.StringIO(imgstring)
    canvas = Image.open(filelike)

    # canvas = FairyImage.getfairypicfromdb(fairy['name'])
    canvas = FairyImage.addFairyNametoImage(canvas, fairy)
    canvas = FairyImage.addFairyChartoImage(canvas, fairy)
    canvas = FairyImage.addFairydetaildstoImage(canvas, fairy)
    output = StringIO.StringIO()
    canvas.save(output, format="JPEG")
    contents = output.getvalue().encode('base64')
    output.close()
    isadmin = current_user.has_role('admin')
    loggedin = current_user.is_authenticated
    return render_template("main.html", contents=urllib.quote(contents.rstrip('\n')),admin =isadmin, auth=loggedin)


if __name__ == '__main__':
    app.run()

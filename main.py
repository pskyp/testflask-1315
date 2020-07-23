import StringIO
import os
import random
import sys
import urllib

from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, cm,landscape
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table, TableStyle, Image
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib import colors
from reportlab.lib.units import inch
import PyPDF2
from PIL import Image
from flask import make_response

from flask import send_file

from flask import send_from_directory
from google.appengine.api import mail
from reportlab.pdfgen import canvas

import FairyImage
import flask_admin
from flask import Flask, url_for, redirect, render_template, request, abort
from flask_admin import helpers as admin_helpers
from flask_admin.contrib import sqla
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, current_user, roles_accepted
from flask_sqlalchemy import SQLAlchemy
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table
sys.path.insert(1, os.path.join(os.path.abspath('.'), "virtenv/lib/python2.7/site-packages"))

CLOUDSQL_PROJECT = 'testflask-1315'
CLOUDSQL_INSTANCE = 'us-central:fairydb'

# Create app
app = Flask(__name__)
# Create database connection object


# Basic Setup flags
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super-secret'
app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_CONFIRMABLE'] = True
app.config['SECURITY_RECOVERABLE'] = True
app.config['SECURITY_CHANGEABLE'] = True
app.config['SECURITY_LOGIN_WITHOUT_CONFIRMATION'] = False

app.config['SECURITY_POST_LOGIN_VIEW'] = '/home'
app.config['SECURITY_POST_REGISTER_VIEW'] = '/postregister'

# password encryption and salt setup
app.config['SECURITY_PASSWORD_HASH'] = 'sha512_crypt'
app.config['SECURITY_PASSWORD_SALT'] = 'fhasdgihwntlgy8f'


SQLALCHEMY_TRACK_MODIFICATIONS = False



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

    def __str__(self):
        return self.name


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    def __str__(self):
        return self.email


# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)





# Un COmment this code to restet the User DB and create an initial admin user : NOTE set app.config['SECURITY_LOGIN_WITHOUT_CONFIRMATION'] = True

# db.create_all()
# user_datastore.create_user(email='Admin', password='Admin',first_name='Admin')
# db.session.commit()
# user_datastore.create_role(name='superuser',description='site admin role')
# user_datastore.create_role(name='user',description='free user')
# role = user_datastore.find_role('superuser')
# user_datastore.add_role_to_user(user_datastore.find_user(email='pierswilcox@gmail.com'),role)
# db.session.commit()



# Create customized model view class
class MyModelView(sqla.ModelView):
    def is_accessible(self):
        if not current_user.is_active or not current_user.is_authenticated:
            return False

        if current_user.has_role('superuser'):
            return True

        return False

    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to redirect users when a view is not accessible.
        """
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for('security.login', next=request.url))


# views

@app.route('/')
def start():
    return render_template("start.html")


# EMAIL SET UP
@security.send_mail_task
def send_email(msg):
    user_address = msg.recipients
    subject1 = msg.subject
    body1 = msg.body

    mail.send_mail(sender="admin@myfairykingdom.com",
                   to=user_address,
                   subject=subject1,
                   body=body1)


# Create admin
admin = flask_admin.Admin(
    app,
    'My Fairy Kingdom',
    base_template='my_main.html',
    template_mode='bootstrap3',
)

# Add model views
admin.add_view(MyModelView(Role, db.session))
admin.add_view(MyModelView(User, db.session))


# define a context processor for merging flask-admin's template context into the
# flask-security views.
@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template=admin.base_template,
        admin_view=admin.index_view,
        h=admin_helpers,
        get_url=url_for
    )


@app.route('/welcome')
def index():
    import StringIO
    # fairy = FairyImage.getrandomfairy()
    # imgstring = fairy['image']
    # filelike = StringIO.StringIO(imgstring)
    # canvas = Image.open(filelike)
    # canvas = FairyImage.addFairyNametoImage(canvas, fairy)
    # output=StringIO.StringIO()
    # canvas.save(output, format="JPEG")
    # contents= output.getvalue().encode('base64')
    # output.close()
    #
    # return render_template("index.html",contents=urllib.quote(contents.rstrip('\n')))
    x = random.randint(1, 3)
    if (x == 1):
        princesses = Image.open("static/Princess_Tabitha.png")
        name = ("Tabitha")
    elif (x == 2):
        princesses = Image.open("static/Princess_Esme.png")
        name = ("Esme")
    else:
        princesses = Image.open("static/Princess_Violet.png")
        name = ("Violet")
    canvas = princesses
    output = StringIO.StringIO()
    canvas.save(output, format="JPEG")
    contents = output.getvalue().encode('base64')
    return render_template("index.html", contents=urllib.quote(contents.rstrip('\n')), Princess_name=name)


@app.route('/login')
def login():
    import StringIO
    fairy = FairyImage.getrandomfairy()
    imgstring = fairy['image']
    filelike = StringIO.StringIO(imgstring)
    canvas = Image.open(filelike)
    canvas = FairyImage.addFairyNametoImage(canvas, fairy)
    output = StringIO.StringIO()
    canvas.save(output, format="JPEG")
    contents = output.getvalue().encode('base64')
    output.close()

    return render_template("index.html", contents=urllib.quote(contents.rstrip('\n')))


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500


@app.route('/postregister')
def postregister():
    return render_template("postregister.html")


@app.route('/home')
def home():
    import StringIO

    fairy = FairyImage.getrandomfairy()
    imgstring = fairy['image']
    filelike = StringIO.StringIO(imgstring)
    canvas = Image.open(filelike)
    canvas = FairyImage.addFairyNametoImage(canvas, fairy)
    output = StringIO.StringIO()
    canvas.save(output, format="JPEG")
    contents = output.getvalue().encode('base64')
    output.close()
    isadmin = current_user.has_role('superuser')
    loggedin = current_user.is_authenticated
    return render_template("main.html", contents=urllib.quote(contents.rstrip('\n')), admin=isadmin, auth=loggedin)


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
    isadmin = current_user.has_role('superuser')
    loggedin = current_user.is_authenticated
    return render_template('montage.html', contents=urllib.quote(contents.rstrip('\n')), admin=isadmin, auth=loggedin)


@app.route('/montage12')
# print first 12 fairies
def montagea12():
    import StringIO
    size = 800, 550
    canvas = FairyImage.getrandomfairysheet(12)
    canvas.thumbnail(size, Image.ANTIALIAS)
    output = StringIO.StringIO()
    canvas.save(output, format="JPEG")
    contents = output.getvalue().encode('base64')
    output.close()
    isadmin = current_user.has_role('superuser')
    loggedin = current_user.is_authenticated
    return render_template('montage12.html', contents=urllib.quote(contents.rstrip('\n')), admin=isadmin, auth=loggedin)


@app.route('/montage100')
# print first 48 fairies
def montage100():
    import StringIO
    size = 1200, 4400
    canvas = FairyImage.getfairysheet(48)
    canvas.thumbnail(size, Image.ANTIALIAS)
    output = StringIO.StringIO()
    canvas.save(output, format="JPEG")
    contents = output.getvalue().encode('base64')
    output.close()
    isadmin = current_user.has_role('superuser')
    loggedin = current_user.is_authenticated
    return render_template('montage100.html', contents=urllib.quote(contents.rstrip('\n')), admin=isadmin,
                           auth=loggedin)


@app.route('/db')
@roles_accepted('superuser')
def db():
    gfairies = FairyImage.numberoffairies('f')
    bfairies = FairyImage.numberoffairies('m')
    tfairies = bfairies + gfairies
    fairyref = FairyImage.getfairyreferences('FAIRY_TBL')
    loggedin = current_user.is_authenticated

    return render_template("dblist.html", gfairies=str(gfairies), bfairies=str(bfairies), tfairies=str(tfairies),
                           fairyref=str(fairyref), auth=loggedin)


@app.route('/deletedbtbl')
@roles_accepted('superuser')
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
@roles_accepted('superuser')
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
@roles_accepted('superuser')
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
    isadmin = current_user.has_role('superuser')
    loggedin = current_user.is_authenticated
    return render_template("main.html", contents=urllib.quote(contents.rstrip('\n')), admin=isadmin, auth=loggedin)


@app.route('/fdetailcard')
def fairydetailcardimage():
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
    isadmin = current_user.has_role('superuser')
    loggedin = current_user.is_authenticated
    return render_template("main.html", contents=urllib.quote(contents.rstrip('\n')), admin=isadmin, auth=loggedin)


@app.route('/pdfcard')
@roles_accepted('superuser')
def pdfcard():

    PAGE_size = 180, 252
    IMG_size = 270, 378



    # use the random ID's to populate a list of Fairies to build card deck from
    fairys = FairyImage.get_multiplerandom_fairies_from_db("FAIRY_TBL", 60)

    x = 0
    pdf = StringIO.StringIO()
    c = canvas.Canvas(pdf, pagesize=PAGE_size)

    #  Build the cards (DOn't know why multiples of 10? but this builds a deck of 54)
    while (x < 60):
        # fairy = FairyImage.get_fairy_from_db("FAIRY_TBL", int(Ids[x]))
        fairy = fairys[x]
        imgstring = fairy['image']
        filelike = StringIO.StringIO(imgstring)
        pic = Image.open(filelike)
        # img = Image(filename=filelike, width=270, height=378)
        pic.thumbnail(IMG_size, Image.ANTIALIAS)
        c.drawInlineImage(pic, 5, 75, width=None, height=None)
        # Get Fairy Details

        name = fairy['name']
        age = fairy['agescore']
        kind = (int(fairy['kindscore'])/2)
        magic = fairy['magicscore']
        agility = fairy['agilityscore']
        charactor = fairy['charactorscore']

                  # define a large font
        c.setFont("Helvetica", 16)
        # choose some colors

        c.setStrokeColorRGB(0.2, 0.5, 0.3)

        # # draw some lines
        # c.line(0, 0, 0, 1.7 * inch)
        # c.line(0, 0, 1 * inch, 0)
        # draw a rectangle
        c.rect(0.1 * inch, 0.1 * inch, 180, 252, fill=0)
        # make text go straight up
        c.rotate(90)
        # change color
        c.setFillColorRGB(0, 0, 0.77)
        # say hello (note after rotate the y coord needs to be negative!)
        c.drawRightString(245, 0.4*-inch, str(name))
        c.rotate(-90)
        # TODO set box to boy or girl colour
        c.setFillColorRGB(.9, .67, .98)
        c.rect(0.1 * inch, 0.1 * inch, 180, 1*inch, fill=1)
        c.setFont("Helvetica", 12)
        c.setFillColorRGB(0, 0, 0.77)
        c.drawString(0.2 * inch, 0.8 * inch, 'Age Index = '+ str(age))
        c.drawString(0.2 * inch, 0.5 * inch,  'Kindness = '+ str(kind))
        c.drawString(0.2 * inch, 0.2 * inch,  'Charactor = '+ str(charactor))
        c.drawRightString(175, 0.8 * inch,  'Magic = '+ str(magic))
        c.drawRightString(175, 0.5 * inch,  'Agility = '+ str(agility))
        # table = Table(data, colWidths=180, rowHeights=252)
        # table.setStyle(TableStyle([
        #     # ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        #     ('BOX', (0, 0), (-1, -1), 2, colors.palevioletred),
        #     # ('BACKGROUND', (0, 0), (-1, 2), colors.lightgrey)
        # ]))

        # table.wrapOn(c, 0, 18)
        # table.drawOn(c, 0, 18)
        #

        c.showPage()
        x = x + 1

    c.save()


    #  Append all teh Cards into a PDF of all the cards for printing out
    input_pdf = PyPDF2.PdfFileReader(pdf)
    output_pdf = PyPDF2.PdfFileWriter()
    # calculate number of A4 paged reguired for 9 fairies per page error control to make sure it prints whole pages
    number_page = input_pdf.getNumPages() % 9

    # get the first page from each pdf


    # start a new blank page with a size that can fit the merged pages side by side

    p = 0
    while (p < number_page):
        page0 = input_pdf.pages[(9 * p) + 0]
        page1 = input_pdf.pages[(9 * p) + 1]
        page2 = input_pdf.pages[(9 * p) + 2]
        page3 = input_pdf.pages[(9 * p) + 3]
        page4 = input_pdf.pages[(9 * p) + 4]
        page5 = input_pdf.pages[(9 * p) + 5]
        page6 = input_pdf.pages[(9 * p) + 6]
        page7 = input_pdf.pages[(9 * p) + 7]
        page8 = input_pdf.pages[(9 * p) + 8]
        # page0 = input_pdf.pages[0]
        # page1 = input_pdf.pages[1]
        # page2 = input_pdf.pages[2]
        # page3 = input_pdf.pages[3]
        # page4 = input_pdf.pages[4]
        # page5 = input_pdf.pages[5]
        # page6 = input_pdf.pages[6]
        # page7 = input_pdf.pages[7]
        # page8 = input_pdf.pages[8]

        page = output_pdf.addBlankPage(width=595, height=843)
        page.mergeTranslatedPage(page0, 0, 0)
        page.mergeTranslatedPage(page1, 198, 0)
        page.mergeTranslatedPage(page2, 396, 0)
        page.mergeTranslatedPage(page3, 0, 273)
        page.mergeTranslatedPage(page4, 198, 273)
        page.mergeTranslatedPage(page5, 396, 273)
        page.mergeTranslatedPage(page6, 0, 546)
        page.mergeTranslatedPage(page7, 198, 546)
        page.mergeTranslatedPage(page8, 396, 546)
        p = p + 1

    # write to file
    outputstream = StringIO.StringIO()
    output_pdf.write(outputstream)


    binary_pdf = outputstream.getvalue()
    outputstream.close()
    response = make_response(binary_pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = \
        'inline; filename=%s.pdf' % 'test.pdf'
    return response


    # return send_file(output_pdf, as_attachment=True)


    # return redirect('/home')



@app.route('/randompdfcard')
@roles_accepted('superuser')
def randompdfcard():

    PAGE_size = 180, 252
    IMG_size = 270, 378

    l = FairyImage.getfairyreferences("FAIRY_TBL")
    numgirl = (len(l[0]))
    numboy = (len(l[1]))

    # Get a list of all Fairy IDs
    Ids = []
    for x in range(0, numgirl - 1):
        Ids.append(l[0][x][0])
    for y in range(0, numboy - 1):
        Ids.append(l[1][y][0])

    # get  Random selection ID's from the list of all ID's
    random_IDs = []


    while (random_IDs.__len__()<60):
        id = random.choice(Ids)
        if id not in random_IDs:
            random_IDs.append(id)

    # use the random ID's to populate a list of Fairies to build card deck from
    fairys = FairyImage.get_multiple_fairies_from_db("FAIRY_TBL", random_IDs)

    x = 0
    pdf = StringIO.StringIO()
    c = canvas.Canvas(pdf, pagesize=PAGE_size)

    #  Build the cards (DOn't know why multiples of 10? but this builds a deck of 54)
    while (x < 60):
        # fairy = FairyImage.get_fairy_from_db("FAIRY_TBL", int(Ids[x]))
        fairy = fairys[x]
        imgstring = fairy['image']
        filelike = StringIO.StringIO(imgstring)
        pic = Image.open(filelike)
        # img = Image(filename=filelike, width=270, height=378)
        pic.thumbnail(IMG_size, Image.ANTIALIAS)
        c.drawInlineImage(pic, 5, 75, width=None, height=None)
        # Get Fairy Details

        name = fairy['name']
        age = fairy['agescore']
        kind = (int(fairy['kindscore'])/2)
        magic = fairy['magicscore']
        agility = fairy['agilityscore']
        charactor = fairy['charactorscore']

                  # define a large font
        c.setFont("Helvetica", 16)
        # choose some colors

        c.setStrokeColorRGB(0.2, 0.5, 0.3)

        # # draw some lines
        # c.line(0, 0, 0, 1.7 * inch)
        # c.line(0, 0, 1 * inch, 0)
        # draw a rectangle
        c.rect(0.1 * inch, 0.1 * inch, 180, 252, fill=0)
        # make text go straight up
        c.rotate(90)
        # change color
        c.setFillColorRGB(0, 0, 0.77)
        # say hello (note after rotate the y coord needs to be negative!)
        c.drawRightString(245, 0.4*-inch, str(name))
        c.rotate(-90)
        # TODO set box to boy or girl colour
        c.setFillColorRGB(.9, .67, .98)
        c.rect(0.1 * inch, 0.1 * inch, 180, 1*inch, fill=1)
        c.setFont("Helvetica", 12)
        c.setFillColorRGB(0, 0, 0.77)
        c.drawString(0.2 * inch, 0.8 * inch, 'Age Index = '+ str(age))
        c.drawString(0.2 * inch, 0.5 * inch,  'Kindness = '+ str(kind))
        c.drawString(0.2 * inch, 0.2 * inch,  'Charactor = '+ str(charactor))
        c.drawRightString(175, 0.8 * inch,  'Magic = '+ str(magic))
        c.drawRightString(175, 0.5 * inch,  'Agility = '+ str(agility))
        # table = Table(data, colWidths=180, rowHeights=252)
        # table.setStyle(TableStyle([
        #     # ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        #     ('BOX', (0, 0), (-1, -1), 2, colors.palevioletred),
        #     # ('BACKGROUND', (0, 0), (-1, 2), colors.lightgrey)
        # ]))

        # table.wrapOn(c, 0, 18)
        # table.drawOn(c, 0, 18)
        #

        c.showPage()
        x = x + 1

    c.save()


    #  Append all teh Cards into a PDF of all the cards for printing out
    input_pdf = PyPDF2.PdfFileReader(pdf)
    output_pdf = PyPDF2.PdfFileWriter()
    # calculate number of A4 paged reguired for 9 fairies per page error control to make sure it prints whole pages
    number_page = input_pdf.getNumPages() % 9

    # get the first page from each pdf


    # start a new blank page with a size that can fit the merged pages side by side

    p = 0
    while (p < number_page):
        page0 = input_pdf.pages[(9 * p) + 0]
        page1 = input_pdf.pages[(9 * p) + 1]
        page2 = input_pdf.pages[(9 * p) + 2]
        page3 = input_pdf.pages[(9 * p) + 3]
        page4 = input_pdf.pages[(9 * p) + 4]
        page5 = input_pdf.pages[(9 * p) + 5]
        page6 = input_pdf.pages[(9 * p) + 6]
        # page7 = input_pdf.pages[(9 * p) + 7]
        # page8 = input_pdf.pages[(9 * p) + 8]
        # page0 = input_pdf.pages[0]
        # page1 = input_pdf.pages[1]
        # page2 = input_pdf.pages[2]
        # page3 = input_pdf.pages[3]
        # page4 = input_pdf.pages[4]
        # page5 = input_pdf.pages[5]
        # page6 = input_pdf.pages[6]
        # page7 = input_pdf.pages[7]
        # page8 = input_pdf.pages[8]

        page = output_pdf.addBlankPage(width=595, height=843)
        page.mergeTranslatedPage(page0, 0, 0)
        page.mergeTranslatedPage(page1, 198, 0)
        page.mergeTranslatedPage(page2, 396, 0)
        page.mergeTranslatedPage(page3, 0, 273)
        page.mergeTranslatedPage(page4, 198, 273)
        page.mergeTranslatedPage(page5, 396, 273)
        page.mergeTranslatedPage(page6, 0, 546)
        # page.mergeTranslatedPage(page7, 198, 546)
        # page.mergeTranslatedPage(page8, 396, 546)
        p = p + 1

    # write to file
    outputstream = StringIO.StringIO()
    output_pdf.write(outputstream)


    binary_pdf = outputstream.getvalue()
    outputstream.close()
    response = make_response(binary_pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = \
        'inline; filename=%s.pdf' % 'test.pdf'
    return response


    # return send_file(output_pdf, as_attachment=True)


    # return redirect('/home')



if __name__ == '__main__':
    app.run(debug=True)

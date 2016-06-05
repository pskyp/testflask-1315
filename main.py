import urllib

import FairyImage
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    import StringIO

    fairy = FairyImage.getrandomfairy()
    canvas = FairyImage.getfairypicfromdb(fairy['name'])
    # canvas = FairyImage.getfairyimage(fairy)
    # canvas = FairyImage.getrandomfairypic()
    canvas = FairyImage.addFairyNametoImage(canvas, fairy)
    output=StringIO.StringIO()
    canvas.save(output,format="PNG")
    contents= output.getvalue().encode('base64')
    output.close()

    return render_template("main.html",contents=urllib.quote(contents.rstrip('\n')))
    # FairyImage.create_fairy_table('FAIRY_TBL')
    # FairyImage.resetDB(100)
    # return ('hello world')


@app.route('/home')
def home():
    import StringIO

    fairy = FairyImage.getrandomfairy()
    canvas = FairyImage.getfairypicfromdb(fairy['name'])
    # canvas = FairyImage.getfairyimage(fairy)
    canvas = FairyImage.addFairyNametoImage(canvas, fairy)
    output=StringIO.StringIO()
    canvas.save(output,format="PNG")
    contents= output.getvalue().encode('base64')
    output.close()

    return render_template("main.html",contents=urllib.quote(contents.rstrip('\n')))


@app.route('/montage20')
def montage20():
    # print 20 random fairies
    import StringIO
    from PIL import Image
    size = 1200, 2000
    canvas = FairyImage.getrandomfairysheet(8)
    canvas.thumbnail(size, Image.ANTIALIAS)
    output = StringIO.StringIO()
    canvas.save(output, format="PNG")

    contents = output.getvalue().encode('base64')
    output.close()

    return render_template('montage.html', contents=urllib.quote(contents.rstrip('\n')))


@app.route('/montage100')
# print first 100 fairies
def montageal00():
    import StringIO
    from PIL import Image
    size = 1200, 10000
    canvas = FairyImage.getfairysheet(12)
    canvas.thumbnail(size, Image.ANTIALIAS)
    output=StringIO.StringIO()
    canvas.save(output,format="PNG")

    contents= output.getvalue().encode('base64')
    output.close()

    return render_template('montage.html', contents=urllib.quote(contents.rstrip('\n')))


@app.route('/db')
def db():
    gfairies = FairyImage.numberoffairies('f')
    bfairies = FairyImage.numberoffairies('m')
    tfairies = bfairies+gfairies
    fairyref = FairyImage.getfairyreferences('FAIRY_TBL')


    return render_template("dblist.html",gfairies=str(gfairies), bfairies=str(bfairies),tfairies=str(tfairies),fairyref=str(fairyref))


@app.route('/deletedbtbl')
def deletedb_TBL():
    FairyImage.delete_table('FAIRY_TBL')

    gfairies = FairyImage.numberoffairies('f')
    bfairies = FairyImage.numberoffairies('m')
    tfairies = bfairies + gfairies
    fairyref = FairyImage.getfairyreferences('FAIRY_TBL')

    return render_template("dblist.html", gfairies=str(gfairies), bfairies=str(bfairies), tfairies=str(tfairies),
                           fairyref=str(fairyref))


@app.route('/createdbtbl')
def createdb_TBL():
    FairyImage.create_fairy_table('FAIRY_TBL')
    gfairies = FairyImage.numberoffairies('f')
    bfairies = FairyImage.numberoffairies('m')
    tfairies = bfairies + gfairies
    fairyref = FairyImage.getfairyreferences('FAIRY_TBL')

    return render_template("dblist.html", gfairies=str(gfairies), bfairies=str(bfairies), tfairies=str(tfairies),
                           fairyref=str(fairyref))


@app.route('/resetdb')
def resetDB():
    FairyImage.resetDB(100)
    gfairies = FairyImage.numberoffairies('f')
    bfairies = FairyImage.numberoffairies('m')
    tfairies = bfairies + gfairies
    fairyref = FairyImage.getfairyreferences('FAIRY_TBL')

    return render_template("dblist.html", gfairies=str(gfairies), bfairies=str(bfairies), tfairies=str(tfairies),
                           fairyref=str(fairyref))


@app.route('/addgfairy')
def addgfairy():
    import StringIO
    newfairy = FairyImage.createfairy('f')
    canvas = FairyImage.getfairyimage(newfairy)
    output = StringIO.StringIO()
    canvas.save(output, format="PNG")
    contents = output.getvalue().encode('base64')
    output.close()

    gfairies = FairyImage.numberoffairies('f')
    bfairies = FairyImage.numberoffairies('m')
    tfairies = bfairies + gfairies
    fairyref = FairyImage.getfairyreferences('FAIRY_TBL')

    return render_template("dblist2.html", gfairies=str(gfairies), bfairies=str(bfairies), tfairies=str(tfairies),
                           fairyref=str(fairyref), contents=urllib.quote(contents.rstrip('\n')))


@app.route('/addbfairy')
def addbfairy():
    import StringIO
    newfairy = FairyImage.createfairy('m')
    canvas = FairyImage.getfairyimage(newfairy)
    output = StringIO.StringIO()
    canvas.save(output, format="PNG")
    contents = output.getvalue().encode('base64')
    output.close()

    gfairies = FairyImage.numberoffairies('f')
    bfairies = FairyImage.numberoffairies('m')
    tfairies = bfairies + gfairies
    fairyref = FairyImage.getfairyreferences('FAIRY_TBL')

    return render_template("dblist2.html", gfairies=str(gfairies), bfairies=str(bfairies), tfairies=str(tfairies),
                           fairyref=str(fairyref), contents=urllib.quote(contents.rstrip('\n')))


@app.route('/fcard')
def fairycardimage():
    import StringIO
    fairy = FairyImage.getrandomfairy()
    canvas = FairyImage.getfairyimage(fairy)
    canvas = FairyImage.addFairyChartoImage(canvas, fairy)
    output = StringIO.StringIO()
    canvas.save(output, format="PNG")
    contents = output.getvalue().encode('base64')
    output.close()

    return render_template("main.html", contents=urllib.quote(contents.rstrip('\n')))


@app.route('/fdetailcard')
def fairydetailcardimage():
    import StringIO
    fairy = FairyImage.getrandomfairy()
    canvas = FairyImage.getfairyimage(fairy)
    canvas = FairyImage.addFairyChartoImage(canvas, fairy)
    canvas = FairyImage.addFairydetaildstoImage(canvas, fairy)
    output = StringIO.StringIO()
    canvas.save(output, format="PNG")
    contents = output.getvalue().encode('base64')
    output.close()

    return render_template("main.html", contents=urllib.quote(contents.rstrip('\n')))


if __name__ == '__main__':
    app.run()

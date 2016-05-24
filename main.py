from flask import Flask
from flask import render_template
import FairyImage
import urllib


app = Flask(__name__)

@app.route('/')
def index():
    import StringIO

    canvas = FairyImage.getrandomfairypic()
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

    canvas = FairyImage.getrandomfairypic()
    output=StringIO.StringIO()
    canvas.save(output,format="PNG")
    contents= output.getvalue().encode('base64')
    output.close()

    return render_template("main.html",contents=urllib.quote(contents.rstrip('\n')))


@app.route('/montage')
def montage():
    import StringIO

    canvas = FairyImage.getfairysheet(6)
    output=StringIO.StringIO()
    canvas.save(output,format="PNG")
    contents= output.getvalue().encode('base64')
    output.close()

    return render_template('montage.html', contents=urllib.quote(contents.rstrip('\n')))


@app.route('/db')
def db():
    import StringIO

    gfairies = FairyImage.numberoffairies('f')
    bfairies = FairyImage.numberoffairies('m')
    tfairies = bfairies+gfairies
    fairyref = FairyImage.getfairyreferences('FAIRY_TBL')


    return render_template("dblist.html",gfairies=str(gfairies), bfairies=str(bfairies),tfairies=str(tfairies),fairyref=str(fairyref))

if __name__ == '__main__':
    app.run()

import StringIO
import getopt
import os
import random
import sys

import pymysql.cursors

CLOUDSQL_PROJECT = 'testflask-1315'
CLOUDSQL_INSTANCE = 'us-central:fairydb'



from PIL import Image, ImageDraw, ImageFont
sys.path.insert(1, os.path.join(os.path.abspath('.'), "virtenv/lib/python2.7/site-packages"))

def personality():
    traits = ["intelligence", "kindness", "fairness", "funness", "wisdom", "dexterity", "humour", "magic", "speed"]
    intelligence = random.randint(50, 75)
    kindness = random.randint(50, 75)
    fairness = random.randint(50, 75)
    funness = random.randint(50, 75)
    wisdom = random.randint(50, 75)
    dexterity = random.randint(50, 75)
    humour = random.randint(50, 75)
    magic = random.randint(50, 75)
    speed = random.randint(50, 75)
    specialabilit1 = traits[random.randint(0, len(traits) - 1)]
    specialabilit2 = traits[random.randint(0, len(traits) - 1)]
    if specialabilit1 == "intelligence":
        intelligence += random.randint(4, 10)
    elif specialabilit1 == "kindness":
        kindness += random.randint(4, 10)
    elif specialabilit1 == "fairness":
        fairness += random.randint(4, 10)
    elif specialabilit1 == "funness":
        funness += random.randint(4, 10)
    elif specialabilit1 == "wisdom":
        wisdom += random.randint(4, 10)
    elif specialabilit1 == "dexterity":
        dexterity += random.randint(4, 10)
    elif specialabilit1 == "humour":
        humour += random.randint(4, 10)
    elif specialabilit1 == "magic":
        magic += random.randint(4, 10)
    elif specialabilit1 == "speed":
        speed += random.randint(4, 10)
    if specialabilit2 == "intelligence":
        intelligence += random.randint(4, 10)
    elif specialabilit2 == "kindness":
        kindness += random.randint(4, 10)
    elif specialabilit2 == "fairness":
        fairness += random.randint(4, 10)
    elif specialabilit2 == "funness":
        funness += random.randint(4, 10)
    elif specialabilit2 == "wisdom":
        wisdom += random.randint(4, 10)
    elif specialabilit2 == "dexterity":
        dexterity += random.randint(4, 10)
    elif specialabilit2 == "humour":
        humour += random.randint(4, 10)
    elif specialabilit2 == "magic":
        magic += random.randint(4, 10)
    elif specialabilit2 == "speed":
        speed += random.randint(4, 10)
    age = int(((random.randint(1, 100) + random.randint(1, 100) + random.randint(1, 85) + random.randint(1,
                                                                                                         100) + random.randint(
        5, 100) + random.randint(5, 100) + random.randint(6, 100)) / 7) / 2)
    charactor = int(((intelligence + kindness + fairness + wisdom + humour) / 5) / 2)
    magicstrength = int((((age + 100) + dexterity + intelligence + magic) / 4) / 2)
    agility = int((((age + 100) + dexterity + speed) / 3) / 2)
    p = dict([(traits[0], intelligence), (traits[1], kindness), (traits[2], fairness), (traits[3], funness),
              (traits[4], wisdom), (traits[5], dexterity), (traits[6], humour), (traits[7], magic), (traits[8], speed),
              ("age", age), ("charactor", charactor), ("magicstrength", magicstrength), ("agility", agility)])
    return p


def name(sex):
    if sex == "m":
        with open("data/boy_fairy_names.txt") as f:

            boynames = []
            for line in f:
                boynames.append(line)
            f.closed
        countofnames = len(boynames)
        selectedfirstname = boynames[random.randint(0, countofnames - 1)]

    else:
        with open("data/girl_fairy_names.txt") as f:
            girlnames = []
            for line in f:
                girlnames.append(line)
            f.closed
        countofnames = len(girlnames)
        selectedfirstname = girlnames[random.randint(0, countofnames - 1)]
    with open("data/fairy_surnames.txt") as f:
        surnames = []
        for line in f:
            surnames.append(line)
        f.closed
    countofsurnames = len(surnames)
    selectedsurname = surnames[random.randint(0, countofsurnames - 1)]
    selectedname = selectedfirstname + " " + selectedsurname
    selectedname = selectedname.replace('\n', '')
    return selectedname.replace('\r', '')


def createfairy(sex):
    if sex == "f":

        bodyx = random.randint(0, 2)  # pick a random row
        bodyy = random.randint(0, 2)  # pick a random column
        wingx = random.randint(0, 9)
        wingy = random.randint(0, 2)
        eyesx = random.randint(0, 4)
        eyesy = random.randint(0, 8)
        mouthsx = random.randint(0, 3)
        mouthsy = random.randint(0, 1)
        earsx = random.randint(0, 2)
        earsy = random.randint(0, 1)
        shoesx = random.randint(0, 10)  # one more so that sometime no shoes are drawn
        shoesy = random.randint(0, 2)
        accessx = random.randint(0, 7)  # three more so that sometime no access are drawn
        accessy = random.randint(0, 1)
        haccessx = random.randint(0, 6)  # four more so that more times no head accessories are drawn
        haccessy = random.randint(0, 1)
        topx = random.randint(0, 10)  # one more column so that some times no top clothes are drawn
        topy = random.randint(0, 2)
        bottomx = random.randint(0, 9)
        bottomy = random.randint(0, 2)
        hairx = random.randint(0, 4)
        hairy = random.randint(0, 9)
        wandx = random.randint(0, 4)
        wandy = random.randint(0, 2)


    elif sex == 'm':
        # picks random sprite based on the size of the boy spreitesheets
        bodyx = random.randint(0, 2)  # pick a random row
        bodyy = random.randint(0, 2)  # pick a random column
        hairx = random.randint(0, 4)
        hairy = random.randint(0, 4)
        wandx = random.randint(0, 4)
        wandy = random.randint(0, 2)
        wingx = random.randint(0, 9)
        wingy = random.randint(0, 2)
        eyesx = random.randint(0, 4)
        eyesy = random.randint(0, 4)
        mouthsx = random.randint(0, 4)
        mouthsy = random.randint(0, 1)
        earsx = random.randint(0, 4)
        earsy = random.randint(0, 1)
        shoesx = random.randint(0, 10)  # one more so that sometime no shoes are drawn
        shoesy = random.randint(0, 2)
        accessx = random.randint(0, 6)  # two more so that sometime no access are drawn
        accessy = random.randint(0, 2)
        haccessx = random.randint(0, 6)  # four more so that more times no head accessories are drawn
        haccessy = random.randint(0, 1)
        topx = random.randint(0, 10)  # one more column so that some times no top clothes are drawn
        topy = random.randint(0, 2)
        bottomx = random.randint(0, 10)  # one more column so that some times no top clothes are drawn
        bottomy = random.randint(0, 2)

        # get personality details
    n = name(sex)
    p = personality()
    fairy = dict([('name', n), ('bodyx', bodyx), ('bodyy', bodyy), ('wingx', wingx),
                  ('wingy', wingy), ('sex', sex), ('eyesx', eyesx), ('eyesy', eyesy), ('mouthsx', mouthsx),
                  ('mouthsy', mouthsy), ('earsx', earsx)
                     , ('earsy', earsy), ('shoesx', shoesx), ('shoesy', shoesy), ('accessx', accessx),
                  ('accessy', accessy),
                  ('haccessx', haccessx), ('haccessy', haccessy), ('topx', topx), ('topy', topy)
                     , ('bottomx', bottomx), ('bottomy', bottomy), ('hairx', hairx), ('hairy', hairy)
                     , ('wandx', wandx), ('wandy', wandy),
                  ('agescore', p["age"]), ('kindscore', p["kindness"]), ('charactorscore', p["charactor"]),
                  ('magicscore', p["magicstrength"]), ('agilityscore', p["agility"]),
                  ('intelligence', p["intelligence"]), ('kindness', p["kindness"]), ('fairness', p["fairness"]),
                  ('funness', p["funness"]), ('wisdom', p["wisdom"]), ('dexterity', p["dexterity"]),
                  ('humour', p["humour"]), ('magic', p["magic"]), ('speed', p["speed"])
                  ])
    add_fairy_to_db('FAIRY_TBL', fairy)

    return fairy


def get_fairy_from_db(dbname, id):
    #  db = pymysql.connect(host='eu-cdbr-azure-west-d.cloudapp.net',
    if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
        con = pymysql.connect(
                    host='104.197.55.21',
                    unix_socket='testflask-1315:fairydb',
                    user='root',
                    passwd='TestFlask',
            database='My_Fairy_Kingdom',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)
    else:

        con = pymysql.connect(host='localhost',
                              user='dbuser',
                              passwd='TestFlask',
                              database='My_Fairy_Kingdom',
                              charset='utf8mb4',
                              cursorclass=pymysql.cursors.DictCursor)
    try:
        with con.cursor(pymysql.cursors.DictCursor) as cursor:
            # Read a single record
            sql = "SELECT * FROM " + dbname + " WHERE `fairyid`=%s"
            cursor.execute(sql, (id,))
            result = cursor.fetchone()
            # if result == None :
            #         return None
            # desc = cursor.description
            # dict ={}

            # for(name,value) in zip(desc,result):
            #         dict[name[0]] =value

            fairy = dict(
                [('name', result['fairyname']), ('bodyx', result['fairybodyX']), ('bodyy', result['fairybodyY']),
                 ('wingx', result['fairywingX']),
                 ('wingy', result['fairywingY']), ('sex', result['fairysex']), ('eyesx', result['fairyeyesX']),
                 ('eyesy', result['fairyeyesY']),
                 ('mouthsx', result['fairymouthX']), ('mouthsy', result['fairymouthY']),
                 ('earsx', result['fairyearsX']), ('earsy', result['fairyearsY']),
                 ('shoesx', result['fairyshoesX']), ('shoesy', result['fairyshoesY']),
                 ('accessx', result['fairyaccessX']), ('accessy', result['fairyaccessY']),
                 ('haccessx', result['fairyheadaccessX']), ('haccessy', result['fairyheadaccessY']),
                 ('topx', result['fairytopX']), ('topy', result['fairytopY']),
                 ('bottomx', result['fairybottomX']), ('bottomy', result['fairybottomY']),
                 ('hairx', result['fairyhairX']), ('hairy', result['fairyhairY']),
                 ('wandx', result['fairywandX']), ('wandy', result['fairywandY']),
                 ('agescore', result["fairyagescore"]),
                 ('kindscore', result["fairykindnessscore"]), ('charactorscore', result["fairycharactorscore"]),
                 ('magicscore', result["fairymagicscore"]), ('agilityscore', result["fairyagilityscore"]),
                 ('intelligence', result["fairyintelligence"]), ('kindness', result["fairykindness"]),
                 ('fairness', result["fairyfairness"]), ('funness', result["fairyfunness"]),
                 ('wisdom', result["fairywisdom"]), ('dexterity', result["fairydexterity"]),
                 ('humour', result["fairyhumour"]), ('magic', result["fairymagic"]), ('speed', result["fairyspeed"])
                 ])
            #print (fairy) 
            return fairy
    finally:
        con.close()


def get_multiple_fairies_from_db(dbname, ids):
    # returns an array of fairies when passed an array of Fiary ID's
    #  db = pymysql.connect(host='eu-cdbr-azure-west-d.cloudapp.net',
    if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
        con = pymysql.connect(
            host='104.197.55.21',
            unix_socket='testflask-1315:fairydb',
            user='root',
            passwd='TestFlask',
            database='My_Fairy_Kingdom',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)
    else:

        con = pymysql.connect(host='localhost',
                              user='dbuser',
                              passwd='TestFlask',
                              database='My_Fairy_Kingdom',
                              charset='utf8mb4',
                              cursorclass=pymysql.cursors.DictCursor)
    try:
        with con.cursor(pymysql.cursors.DictCursor) as cursor:
            # Read a single record
            x = 0
            fairies = []
            id_array = ids
            lenght = int(len(id_array))
            while x < lenght:
                sql = "SELECT * FROM " + dbname + " WHERE `fairyid`=%s"
                cursor.execute(sql, (ids[x],))
                result = cursor.fetchone()
                # if result == None :
                #         return None
                # desc = cursor.description
                # dict ={}

                # for(name,value) in zip(desc,result):
                #         dict[name[0]] =value

                fairy = dict(
                    [('name', result['fairyname']), ('bodyx', result['fairybodyX']), ('bodyy', result['fairybodyY']),
                     ('wingx', result['fairywingX']),
                     ('wingy', result['fairywingY']), ('sex', result['fairysex']), ('eyesx', result['fairyeyesX']),
                     ('eyesy', result['fairyeyesY']),
                     ('mouthsx', result['fairymouthX']), ('mouthsy', result['fairymouthY']),
                     ('earsx', result['fairyearsX']), ('earsy', result['fairyearsY']),
                     ('shoesx', result['fairyshoesX']), ('shoesy', result['fairyshoesY']),
                     ('accessx', result['fairyaccessX']), ('accessy', result['fairyaccessY']),
                     ('haccessx', result['fairyheadaccessX']), ('haccessy', result['fairyheadaccessY']),
                     ('topx', result['fairytopX']), ('topy', result['fairytopY']),
                     ('bottomx', result['fairybottomX']), ('bottomy', result['fairybottomY']),
                     ('hairx', result['fairyhairX']), ('hairy', result['fairyhairY']),
                     ('wandx', result['fairywandX']), ('wandy', result['fairywandY']),
                     ('agescore', result["fairyagescore"]),
                     ('kindscore', result["fairykindnessscore"]), ('charactorscore', result["fairycharactorscore"]),
                     ('magicscore', result["fairymagicscore"]), ('agilityscore', result["fairyagilityscore"]),
                     ('intelligence', result["fairyintelligence"]), ('kindness', result["fairykindness"]),
                     ('fairness', result["fairyfairness"]), ('funness', result["fairyfunness"]),
                     ('wisdom', result["fairywisdom"]), ('dexterity', result["fairydexterity"]),
                     ('humour', result["fairyhumour"]), ('magic', result["fairymagic"]), ('speed', result["fairyspeed"])
                     ])
                # print (fairy)
                fairies.append(fairy)
                x = x + 1
            return fairies
    finally:
        con.close()





# TODO delete Fairy from file

# TODO CREATE SPROTE SHEET TABLE
#  TODO SAVE SPRITESHEET
# TODO LOAD SPRITE SHEET

def create_ssheet_table(dbname):
    #  db = pymysql.connect(host='eu-cdbr-azure-west-d.cloudapp.net',
    if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
        con = pymysql.connect(
                    host='104.197.55.21',
                    unix_socket='testflask-1315:fairydb',
                    user='root',
                    passwd='TestFlask',
            database='My_Fairy_Kingdom',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)
    else:

        con = pymysql.connect(host='localhost',
                              user='dbuser',
                              passwd='TestFlask',
                              database='My_Fairy_Kingdom',
                              charset='utf8mb4',
                              cursorclass=pymysql.cursors.DictCursor)
    # prepare a cursor object using cursor() method
    cursor = con.cursor()

    # Create table as per requirement, check if it already exists
    sql = "CREATE TABLE IF NOT EXISTS " + dbname + """ (
        idSPRITESHEET INT NOT NULL AUTO_INCREMENT,
        SPRITESHEET_NAME VARCHAR(45) NOT NULL,
        SS_UPLOADED_DATE DATE,
        ELEMENT_COUNT INT NOT NULL,
        ROW_COUNT INT NOT NULL,
        COL_COUNT INT NOT NULL,
        # BLOB BLOB NOT NULL,
        PRIMARY KEY(idSPRITESHEET))"""

    cursor.execute(sql)

    # disconnect from server
    con.close()


def create_fairy_table(dbname):
    #  db = pymysql.connect(host='eu-cdbr-azure-west-d.cloudapp.net',
    if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
        con = pymysql.connect(
                    host='104.197.55.21',
                    unix_socket='testflask-1315:fairydb',
                    user='root',
                    passwd='TestFlask',
            database='My_Fairy_Kingdom',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)
    else:

        con = pymysql.connect(host='localhost',
                              user='dbuser',
                              passwd='TestFlask',
                              database='My_Fairy_Kingdom',
                              charset='utf8mb4',
                              cursorclass=pymysql.cursors.DictCursor)
    # prepare a cursor object using cursor() method
    cursor = con.cursor()

    # Create table as per requirement, check if it already exists

   
    sql = "CREATE TABLE IF NOT EXISTS " + dbname + """ (
        fairyid INT NOT NULL AUTO_INCREMENT,
        fairyname VARCHAR(45) NOT NULL,
        fairysex CHARACTER(1) NOT NULL,
        fairybirthday DATE,
        fairycreated DATETIME,
        fairyupdated DATETIME,
        fairybodyX INT,
        fairybodyY INT,
        fairywingX INT,
        fairywingY INT,
        fairytopX INT,
        fairytopY INT,
        fairyshoesX INT,
        fairyshoesY INT,
        fairybottomX INT,
        fairybottomY INT,
        fairymouthX INT,
        fairymouthY INT,
        fairyeyesX INT,
        fairyeyesY INT,
        fairyhairX INT,
        fairyhairY INT,
        fairyearsX INT,
        fairyearsY INT,
        fairyheadaccessX INT,
        fairyheadaccessY INT,
        fairyaccessX INT,
        fairyaccessY INT,
        fairywandX INT,
        fairywandY INT,
        fairyagescore INT,
        fairykindnessscore INT,
        fairycharactorscore INT,
        fairymagicscore INT,
        fairyagilityscore INT,
        fairyintelligence INT,
        fairykindness INT,
        fairyfairness INT,
        fairyfunness INT,
        fairywisdom INT,
        fairydexterity INT,
        fairyhumour INT,
        fairymagic INT,
        fairyspeed INT,
        image MEDIUMBLOB,
    PRIMARY KEY(fairyid)
  )"""

    cursor.execute(sql)

    # disconnect from server
    con.close()


def delete_table(dbname):
     #  db = pymysql.connect(host='eu-cdbr-azure-west-d.cloudapp.net',
    if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
        con = pymysql.connect(
                    host='104.197.55.21',
                    unix_socket='testflask-1315:fairydb',
                    user='root',
                    passwd='TestFlask',
            database='My_Fairy_Kingdom',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)
    else:

        con = pymysql.connect(host='localhost',
                              user='dbuser',
                              passwd='TestFlask',
                              database='My_Fairy_Kingdom',
                              charset='utf8mb4',
                              cursorclass=pymysql.cursors.DictCursor)
    # prepare a cursor object using cursor() method
    cursor = con.cursor()

    # Create table as per requirement, check if it already exists
    sql = "DROP TABLE " + dbname
    cursor.execute(sql)

    # disconnect from server
    con.close()


def add_fairy_to_db(dbname, fairy):
    import StringIO
    # Connect to the database
    #  db = pymysql.connect(host='eu-cdbr-azure-west-d.cloudapp.net',
    canvas = getfairyimage(fairy)
    out = StringIO.StringIO()
    canvas.save(out, "PNG")
    o = out.getvalue()



    if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
        con = pymysql.connect(
                    host='104.197.55.21',
                    unix_socket='testflask-1315:fairydb',
                    user='root',
                    passwd='TestFlask',
            database='My_Fairy_Kingdom',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)
    else:

        con = pymysql.connect(host='localhost',
                              user='dbuser',
                              passwd='TestFlask',
                              database='My_Fairy_Kingdom',
                              charset='utf8mb4',
                              cursorclass=pymysql.cursors.DictCursor)
    # prepare a cursor object using cursor() method

    try:
        with con.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO " + dbname + "(`fairyname`, `fairysex`,`fairybodyX`,`fairybodyY`,`fairywingX`,`fairywingY`,`fairytopX`,`fairytopY`,`fairyshoesX`,`fairyshoesY`,`fairybottomX`,`fairybottomY`,`fairymouthX`,`fairymouthY`,`fairyeyesX`,`fairyeyesY`,`fairyhairX`,`fairyhairY`,`fairyearsX`,`fairyearsY`,`fairyheadaccessX`,`fairyheadaccessY`,`fairyaccessX`,`fairyaccessY`,`fairywandx`,`fairywandy`,`fairyagescore`,`fairykindnessscore`,`fairycharactorscore`,`fairymagicscore`,`fairyagilityscore`,`fairyintelligence`,`fairykindness`,`fairyfairness`,`fairyfunness`,`fairywisdom`,`fairydexterity`,`fairyhumour`,`fairymagic`,`fairyspeed`,`image`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s)"

            cursor.execute(sql,
                           (fairy['name'], fairy['sex'], fairy['bodyx'], fairy['bodyy'], fairy['wingx'], fairy['wingy'],
                            fairy['topx'], fairy['topy'], fairy['shoesx'], fairy['shoesy'], fairy['bottomx'],
                            fairy['bottomy'], fairy['mouthsx'], fairy['mouthsy'], fairy['eyesx'], fairy['eyesy'],
                            fairy['hairx'], fairy['hairy'], fairy['earsx'], fairy['earsy'], fairy['haccessx'],
                            fairy['haccessy'], fairy['accessx'], fairy['accessy'], fairy['wandx'], fairy['wandy'],
                            fairy['agescore'], fairy['kindscore'], fairy['charactorscore'], fairy['magicscore'],
                            fairy['agilityscore'],
                            fairy['intelligence'], fairy['kindness'], fairy['fairness'], fairy['funness'],
                            fairy['wisdom'], fairy['dexterity'], fairy['humour'], fairy['magic'], fairy['speed'], (o,)))

            con.commit()

    finally:
        con.close()
    return


def getfairyimage(fairy, *arg):
    wingssheet = Image.open("SpriteSheets/wings.png")
    if fairy["sex"] == "f":
        # load girl spefific spritesheets
        bodysheet = Image.open("SpriteSheets/girl_fairy_base.png")
        eyessheet = Image.open("SpriteSheets/girls_eyes.png")
        hairsheet = Image.open("SpriteSheets/girls_hair.png")

        wandsheet = Image.open("SpriteSheets/girls_wands.png")
        mouthsheet = Image.open("SpriteSheets/girls_mouths.png")
        earsheet = Image.open("SpriteSheets/girls_ears.png")
        shoessheet = Image.open("SpriteSheets/girls_shoes.png")
        accesssheet = Image.open("SpriteSheets/girls_access.png")
        haccesssheet = Image.open("SpriteSheets/girls_head_access.png")
        topsheet = Image.open("SpriteSheets/girls_top_clothes.png")
        bottomsheet = Image.open("SpriteSheets/girls_bottom_clothes.png")

        # using relevent random row and column result for each spritesheet *
        # adjust the offset according to size of sprite
        body = bodysheet.crop(
            (fairy['bodyx'] * 350, fairy['bodyy'] * 500, (fairy['bodyx'] * 350) + 350, (fairy['bodyy'] * 500) + 500))
        wing = wingssheet.crop(
            (fairy['wingx'] * 400, fairy['wingy'] * 400, (fairy['wingx'] * 400) + 400, (fairy['wingy'] * 400) + 400))
        eyes = eyessheet.crop(
            (fairy['eyesx'] * 350, fairy['eyesy'] * 500, (fairy['eyesx'] * 350) + 350, (fairy['eyesy'] * 500) + 500))
        hair = hairsheet.crop(
            (fairy['hairx'] * 350, fairy['hairy'] * 500, (fairy['hairx'] * 350) + 350, (fairy['hairy'] * 500) + 500))
        wand = wandsheet.crop((fairy['wandx'] * 350, fairy['wandy'] * 500, (fairy['wandx'] * 350) + 350,
                               (fairy['wandy'] * 500) + 500))
        mouth = mouthsheet.crop((fairy['mouthsx'] * 350, fairy['mouthsy'] * 500, (fairy['mouthsx'] * 350)
                                 + 350, (fairy['mouthsy'] * 500) + 500))
        ears = earsheet.crop(
            (fairy['earsx'] * 350, fairy['earsy'] * 500, (fairy['earsx'] * 350) + 350, (fairy['earsy'] * 500) + 500))
        shoes = shoessheet.crop((fairy['shoesx'] * 350, fairy['shoesy'] * 500, (fairy['shoesx'] * 350) + 350,
                                 (fairy['shoesy'] * 500) + 500))
        access = accesssheet.crop((fairy['accessx'] * 350, fairy['accessy'] * 500, (fairy['accessx'] * 350) + 350,
                                   (fairy['accessy'] * 500) + 500))
        haccess = haccesssheet.crop((fairy['haccessx'] * 350, fairy['haccessy'] * 500, (fairy['haccessx']
                                                                                        * 350) + 350,
                                     (fairy['haccessy'] * 500) + 500))
        top = topsheet.crop(
            (fairy['topx'] * 350, fairy['topy'] * 500, (fairy['topx'] * 350) + 350, (fairy['topy'] * 500) + 500))
        bottom = bottomsheet.crop((fairy['bottomx'] * 350, fairy['bottomy'] * 500, (fairy['bottomx'] * 350) + 350,
                                   (fairy['bottomy'] * 500) + 500))

        # blank canvas then the layers pasted onto it, offest to line up with
        # the base body
        canvas = Image.new('RGBA', (800, 550), (255, 255, 255, 255))  # Empty canvas colour (r,g,b,a)?
        canvas.paste(wing, (120, 50), wing)
        canvas.paste(body, (100, 30), body)

        canvas.paste(shoes, (100, 30), shoes)
        canvas.paste(bottom, (100, 30), bottom)
        canvas.paste(top, (100, 30), top)
        canvas.paste(mouth, (100, 30), mouth)
        canvas.paste(eyes, (100, 30), eyes)
        canvas.paste(hair, (100, 30), hair)
        # canvas.paste(ears, (100, 30), ears)
        canvas.paste(haccess, (100, 30), haccess)
        canvas.paste(access, (100, 30), access)
        canvas.paste(wand, (100, 30), wand)

        # ADD FAIRY NAME



    elif fairy["sex"] == "m":
        bodysheet = Image.open("SpriteSheets/boys_fairy_base.png")
        hairsheet = Image.open("SpriteSheets/boys_hair.png")
        wandsheet = Image.open("SpriteSheets/boys_wands.png")
        eyessheet = Image.open("SpriteSheets/boys_eyes.png")
        mouthsheet = Image.open("SpriteSheets/boys_mouths.png")
        earsheet = Image.open("SpriteSheets/boys_ears.png")
        shoessheet = Image.open("SpriteSheets/boys_shoes.png")
        accesssheet = Image.open("SpriteSheets/boys_access.png")
        haccesssheet = Image.open("SpriteSheets/boys_head_access.png")
        topsheet = Image.open("SpriteSheets/boys_top_clothes.png")
        bottomsheet = Image.open("SpriteSheets/boys_bottom_clothes.png")
        body = bodysheet.crop(
            (fairy['bodyx'] * 300, fairy['bodyy'] * 500, (fairy['bodyx'] * 300) + 300, (fairy['bodyy'] * 500) + 500))
        hair = hairsheet.crop(
            (fairy['hairx'] * 200, fairy['hairy'] * 200, (fairy['hairx'] * 200) + 200, (fairy['hairy'] * 200) + 200))
        wand = wandsheet.crop(
            (fairy['wandx'] * 200, fairy['wandy'] * 200, (fairy['wandx'] * 200) + 200, (fairy['wandy'] * 200) + 200))
        wing = wingssheet.crop(
            (fairy['wingx'] * 400, fairy['wingy'] * 400, (fairy['wingx'] * 400) + 400, (fairy['wingy'] * 400) + 400))
        eyes = eyessheet.crop(
            (fairy['eyesx'] * 300, fairy['eyesy'] * 200, (fairy['eyesx'] * 300) + 300, (fairy['eyesy'] * 200) + 200))
        mouth = mouthsheet.crop((fairy['mouthsx'] * 150, fairy['mouthsy'] * 150, (fairy['mouthsx'] * 150) + 150,
                                 (fairy['mouthsy'] * 150) + 150))
        ears = earsheet.crop(
            (fairy['earsx'] * 100, fairy['earsy'] * 140, (fairy['earsx'] * 100) + 100, (fairy['earsy'] * 140) + 140))
        shoes = shoessheet.crop((fairy['shoesx'] * 200, fairy['shoesy'] * 200, (fairy['shoesx'] * 200) + 200,
                                 (fairy['shoesy'] * 200) + 200))
        access = accesssheet.crop((fairy['accessx'] * 300, fairy['accessy'] * 300, (fairy['accessx'] * 300) + 300,
                                   (fairy['accessy'] * 300) + 300))
        haccess = haccesssheet.crop((fairy['haccessx'] * 302, fairy['haccessy'] * 264, (fairy['haccessx'] * 302) + 302,
                                     (fairy['haccessy'] * 264) + 264))
        top = topsheet.crop(
            (fairy['topx'] * 300, fairy['topy'] * 500, (fairy['topx'] * 300) + 300, (fairy['topy'] * 500) + 500))
        bottom = bottomsheet.crop((fairy['bottomx'] * 300, fairy['bottomy'] * 500, (fairy['bottomx'] * 300) + 300,
                                   (fairy['bottomy'] * 500) + 500))

        # blank canvas then the layers pasted onto it, offest to line up with
        # the base body
        canvas = Image.new('RGBA', (800, 550), (255, 255, 255, 255))  # Empty canvas colour (r,g,b,a)?
        canvas.paste(wing, (110, 50), wing)
        canvas.paste(body, (100, 30), body)
        canvas.paste(top, (100, 30), top)
        canvas.paste(shoes, (150, 330), shoes)
        canvas.paste(bottom, (100, 30), bottom)
        canvas.paste(mouth, (160, 113), mouth)
        canvas.paste(eyes, (74, 20), eyes)
        canvas.paste(hair, (150, 30), hair)
        canvas.paste(ears, (275, 75), ears)
        canvas.paste(haccess, (114, -15), haccess)
        canvas.paste(access, (99, 116), access)
        canvas.paste(wand, (193, 163), wand)

    # draw = ImageDraw.Draw(canvas)
    # titlefont = ImageFont.truetype("data/Arial.ttf", 30)
    # draw.text((150, 0), fairy['name'], (0, 0, 0), font=titlefont)
    # draw.text((150, 550), "Age Index :" + str(fairy['agescore']), (0, 0, 0), font=titlefont)
    # draw.text((150, 580), "Kindness :" + str(int(fairy['kindscore'] / 2)), (0, 0, 0), font=titlefont)
    # draw.text((150, 610), "Charactor :" + str(fairy['charactorscore']), (0, 0, 0), font=titlefont)
    # draw.text((150, 640), "Magic Strength :" + str(fairy['magicscore']), (0, 0, 0), font=titlefont)
    # draw.text((150, 670), "Agility :" + str(fairy["agilityscore"]), (0, 0, 0), font=titlefont)
    #
    # if len(arg) == 1:
    #     if arg[0] == "d":
    #         font = ImageFont.truetype("data/Arial.ttf", 16)
    #         draw.text((475, 0), "Body ref: =" + str(fairy['bodyx']) + "," + str(fairy['bodyy']), (0, 0, 0), font=font)
    #         draw.text((475, 20), "Hair ref: =" + str(fairy['hairx']) + "," + str(fairy['hairy']), (0, 0, 0), font=font)
    #         draw.text((475, 40), "Wand ref: =" + str(fairy['wandx']) + "," + str(fairy['wandy']), (0, 0, 0), font=font)
    #         draw.text((475, 60), "Wings ref: =" + str(fairy['wingx']) + "," + str(fairy['wingy']), (0, 0, 0), font=font)
    #         draw.text((475, 80), "eyes ref: =" + str(fairy['eyesx']) + "," + str(fairy['eyesy']), (0, 0, 0), font=font)
    #         draw.text((475, 100), "mouth ref: =" + str(fairy['mouthsx']) + "," + str(fairy['mouthsy']), (0, 0, 0),
    #                   font=font)
    #         draw.text((475, 120), "ears ref: =" + str(fairy['earsx']) + "," + str(fairy['earsy']), (0, 0, 0), font=font)
    #         draw.text((475, 140), "shoe ref: =" + str(fairy['shoesx']) + "," + str(fairy['shoesy']), (0, 0, 0),
    #                   font=font)
    #         draw.text((475, 160), "access ref: =" + str(fairy['accessx']) + "," + str(fairy['accessy']), (0, 0, 0),
    #                   font=font)
    #         draw.text((475, 180), "head access ref: =" + str(fairy['haccessx']) + "," + str(fairy['haccessy']),
    #                   # (0, 0, 0), font=font)
    #         draw.text((475, 200), "top clothes ref: =" + str(fairy['topx']) + "," + str(fairy['topy']), (0, 0, 0),
    #                   font=font)
    #         draw.text((475, 220), "bottom clothes ref: =" + str(fairy['bottomx']) + "," + str(fairy['bottomy']),
    #                   (0, 0, 0), font=font)

    return canvas


def createlotsfairies(number, sex):
    x = 0
    while x < number:
        createfairy(sex)
        x += 1
    return


def getfairyIDfromname(name):
    #  db = pymysql.connect(host='eu-cdbr-azure-west-d.cloudapp.net',
    if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
        con = pymysql.connect(
                    host='104.197.55.21',
                    unix_socket='testflask-1315:fairydb',
                    user='root',
                    passwd='TestFlask',
            database='My_Fairy_Kingdom',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)
    else:

        con = pymysql.connect(host='localhost',
                              user='dbuser',
                              passwd='TestFlask',
                              database='My_Fairy_Kingdom',
                              charset='utf8mb4',
                              cursorclass=pymysql.cursors.DictCursor)
    # prepare a cursor object using cursor() method

    try:
        with con.cursor(pymysql.cursors.DictCursor) as cursor:

            sql = "SELECT `fairyid` FROM `FAIRY_TBL` WHERE `fairyname`=%s"
            cursor.execute(sql, (name,))
            result = cursor.fetchone()
    finally:
        con.close()
    return result

def getfairyreferences(dbname):
    girlarray = []
    boyarray = []

    # Connect to the database



    #  db = pymysql.connect(host='eu-cdbr-azure-west-d.cloudapp.net',
    if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
        con = pymysql.connect(
                    host='104.197.55.21',
                    unix_socket='testflask-1315:fairydb',
                    user='root',
                    passwd='TestFlask',
            database='My_Fairy_Kingdom',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)
    else:

        con = pymysql.connect(host='localhost',
                              user='dbuser',
                              passwd='TestFlask',
                              database='My_Fairy_Kingdom',
                              charset='utf8mb4',
                              cursorclass=pymysql.cursors.DictCursor)
    # prepare a cursor object using cursor() method


    try:
        with con.cursor(pymysql.cursors.DictCursor) as cursor:
            # Read all girlfairy records
            sql = "SELECT `fairyid`,`fairyname` FROM " + dbname + " WHERE `fairysex`=%s"
            cursor.execute(sql, ('f',))
            result = cursor.fetchall()

            for row in result:
                girlarray.append([row['fairyid'], [row['fairyname']]])

        with con.cursor(pymysql.cursors.DictCursor) as cursor:
            # Read all boy fairy records
            sql = "SELECT `fairyid`,`fairyname` FROM " + dbname + " WHERE `fairysex`=%s"
            cursor.execute(sql, ('m',))
            result = cursor.fetchall()

            for row in result:
                boyarray.append([row['fairyid'], [row['fairyname']]])


    finally:
        con.close()

    fairyref = [girlarray, boyarray]
    return fairyref


def numberoffairies(type):
    fairyreferences = getfairyreferences('FAIRY_TBL')
    number = 0
    if type == 'f':
        number = fairyreferences[0].__len__()
    if type == 'm':
        number = fairyreferences[1].__len__()
    if type == 'all':
        number = fairyreferences[1].__len__() + fairyreferences[0].__len__()
    return number


def drawfairytofile(fairy, *arg):
    wingssheet = Image.open("SpriteSheets/wings.png")

    if fairy["sex"] == "f":
        # load girl spefific spritesheets
        bodysheet = Image.open("SpriteSheets/girl_fairy_base.png")
        eyessheet = Image.open("SpriteSheets/girls_eyes.png")
        hairsheet = Image.open("SpriteSheets/girls_hair.png")

        wandsheet = Image.open("SpriteSheets/girls_wands.png")
        mouthsheet = Image.open("SpriteSheets/girls_mouths.png")
        earsheet = Image.open("SpriteSheets/girls_ears.png")
        shoessheet = Image.open("SpriteSheets/girls_shoes.png")
        accesssheet = Image.open("SpriteSheets/girls_access.png")
        haccesssheet = Image.open("SpriteSheets/girls_head_access.png")
        topsheet = Image.open("SpriteSheets/girls_top_clothes.png")
        bottomsheet = Image.open("SpriteSheets/girls_bottom_clothes.png")

        # using relevent random row and column result for each spritesheet *
        # adjust the offset according to size of sprite
        body = bodysheet.crop(
            (fairy['bodyx'] * 350, fairy['bodyy'] * 500, (fairy['bodyx'] * 350) + 350, (fairy['bodyy'] * 500) + 500))
        wing = wingssheet.crop(
            (fairy['wingx'] * 400, fairy['wingy'] * 400, (fairy['wingx'] * 400) + 400, (fairy['wingy'] * 400) + 400))
        eyes = eyessheet.crop(
            (fairy['eyesx'] * 350, fairy['eyesy'] * 500, (fairy['eyesx'] * 350) + 350, (fairy['eyesy'] * 500) + 500))
        hair = hairsheet.crop(
            (fairy['hairx'] * 350, fairy['hairy'] * 500, (fairy['hairx'] * 350) + 350, (fairy['hairy'] * 500) + 500))
        wand = wandsheet.crop((fairy['wandx'] * 350, fairy['wandy'] * 500, (fairy['wandx'] * 350) + 350,
                               (fairy['wandy'] * 500) + 500))
        mouth = mouthsheet.crop((fairy['mouthsx'] * 350, fairy['mouthsy'] * 500, (fairy['mouthsx'] * 350)
                                 + 350, (fairy['mouthsy'] * 500) + 500))
        ears = earsheet.crop(
            (fairy['earsx'] * 350, fairy['earsy'] * 500, (fairy['earsx'] * 350) + 350, (fairy['earsy'] * 500) + 500))
        shoes = shoessheet.crop((fairy['shoesx'] * 350, fairy['shoesy'] * 500, (fairy['shoesx'] * 350) + 350,
                                 (fairy['shoesy'] * 500) + 500))
        access = accesssheet.crop((fairy['accessx'] * 350, fairy['accessy'] * 500, (fairy['accessx'] * 350) + 350,
                                   (fairy['accessy'] * 500) + 500))
        haccess = haccesssheet.crop((fairy['haccessx'] * 350, fairy['haccessy'] * 500, (fairy['haccessx']
                                                                                        * 350) + 350,
                                     (fairy['haccessy'] * 500) + 500))
        top = topsheet.crop(
            (fairy['topx'] * 350, fairy['topy'] * 500, (fairy['topx'] * 350) + 350, (fairy['topy'] * 500) + 500))
        bottom = bottomsheet.crop((fairy['bottomx'] * 350, fairy['bottomy'] * 500, (fairy['bottomx'] * 350) + 350,
                                   (fairy['bottomy'] * 500) + 500))

        # blank canvas then the layers pasted onto it, offest to line up with
        # the base body
        canvas = Image.new('RGBA', (800, 800), (255, 255, 255, 255))  # Empty canvas colour (r,g,b,a)?
        canvas.paste(wing, (120, 50), wing)
        canvas.paste(body, (100, 30), body)

        canvas.paste(shoes, (100, 30), shoes)
        canvas.paste(bottom, (100, 30), bottom)
        canvas.paste(top, (100, 30), top)
        canvas.paste(mouth, (100, 30), mouth)
        canvas.paste(eyes, (100, 30), eyes)
        canvas.paste(hair, (100, 30), hair)
        # canvas.paste(ears, (100, 30), ears)
        canvas.paste(haccess, (100, 30), haccess)
        canvas.paste(access, (100, 30), access)
        canvas.paste(wand, (100, 30), wand)

        # ADD FAIRY NAME



    elif fairy["sex"] == "m":
        bodysheet = Image.open("SpriteSheets/boys_fairy_base.png")
        hairsheet = Image.open("SpriteSheets/boys_hair.png")
        wandsheet = Image.open("SpriteSheets/boys_wands.png")
        eyessheet = Image.open("SpriteSheets/boys_eyes.png")
        mouthsheet = Image.open("SpriteSheets/boys_mouths.png")
        earsheet = Image.open("SpriteSheets/boys_ears.png")
        shoessheet = Image.open("SpriteSheets/boys_shoes.png")
        accesssheet = Image.open("SpriteSheets/boys_access.png")
        haccesssheet = Image.open("SpriteSheets/boys_head_access.png")
        topsheet = Image.open("SpriteSheets/boys_top_clothes.png")
        bottomsheet = Image.open("SpriteSheets/boys_bottom_clothes.png")
        body = bodysheet.crop(
            (fairy['bodyx'] * 300, fairy['bodyy'] * 500, (fairy['bodyx'] * 300) + 300, (fairy['bodyy'] * 500) + 500))
        hair = hairsheet.crop(
            (fairy['hairx'] * 200, fairy['hairy'] * 200, (fairy['hairx'] * 200) + 200, (fairy['hairy'] * 200) + 200))
        wand = wandsheet.crop(
            (fairy['wandx'] * 200, fairy['wandy'] * 200, (fairy['wandx'] * 200) + 200, (fairy['wandy'] * 200) + 200))
        wing = wingssheet.crop(
            (fairy['wingx'] * 400, fairy['wingy'] * 400, (fairy['wingx'] * 400) + 400, (fairy['wingy'] * 400) + 400))
        eyes = eyessheet.crop(
            (fairy['eyesx'] * 300, fairy['eyesy'] * 200, (fairy['eyesx'] * 300) + 300, (fairy['eyesy'] * 200) + 200))
        mouth = mouthsheet.crop((fairy['mouthsx'] * 150, fairy['mouthsy'] * 150, (fairy['mouthsx'] * 150) + 150,
                                 (fairy['mouthsy'] * 150) + 150))
        ears = earsheet.crop(
            (fairy['earsx'] * 100, fairy['earsy'] * 140, (fairy['earsx'] * 100) + 100, (fairy['earsy'] * 140) + 140))
        shoes = shoessheet.crop((fairy['shoesx'] * 200, fairy['shoesy'] * 200, (fairy['shoesx'] * 200) + 200,
                                 (fairy['shoesy'] * 200) + 200))
        access = accesssheet.crop((fairy['accessx'] * 300, fairy['accessy'] * 300, (fairy['accessx'] * 300) + 300,
                                   (fairy['accessy'] * 300) + 300))
        haccess = haccesssheet.crop((fairy['haccessx'] * 302, fairy['haccessy'] * 264, (fairy['haccessx'] * 302) + 302,
                                     (fairy['haccessy'] * 264) + 264))
        top = topsheet.crop(
            (fairy['topx'] * 300, fairy['topy'] * 500, (fairy['topx'] * 300) + 300, (fairy['topy'] * 500) + 500))
        bottom = bottomsheet.crop((fairy['bottomx'] * 300, fairy['bottomy'] * 500, (fairy['bottomx'] * 300) + 300,
                                   (fairy['bottomy'] * 500) + 500))

        # blank canvas then the layers pasted onto it, offest to line up with
        # the base body
        canvas = Image.new('RGBA', (800, 800), (255, 255, 255, 255))  # Empty canvas colour (r,g,b,a)?
        canvas.paste(wing, (110, 50), wing)
        canvas.paste(body, (100, 30), body)
        canvas.paste(top, (100, 30), top)
        canvas.paste(shoes, (150, 330), shoes)
        canvas.paste(bottom, (100, 30), bottom)
        canvas.paste(mouth, (160, 113), mouth)
        canvas.paste(eyes, (74, 20), eyes)
        canvas.paste(hair, (150, 30), hair)
        canvas.paste(ears, (275, 75), ears)
        canvas.paste(haccess, (114, -15), haccess)
        canvas.paste(access, (99, 116), access)
        canvas.paste(wand, (193, 163), wand)

    draw = ImageDraw.Draw(canvas)
    titlefont = ImageFont.truetype("data/Arial.ttf", 30)
    draw.text((150, 0), fairy['name'], (0, 0, 0), font=titlefont)
    draw.text((150, 550), "Age Index :" + str(fairy['agescore']), (0, 0, 0), font=titlefont)
    draw.text((150, 580), "Kindness :" + str(int(fairy['kindscore'] / 2)), (0, 0, 0), font=titlefont)
    draw.text((150, 610), "Charactor :" + str(fairy['charactorscore']), (0, 0, 0), font=titlefont)
    draw.text((150, 640), "Magic Strength :" + str(fairy['magicscore']), (0, 0, 0), font=titlefont)
    draw.text((150, 670), "Agility :" + str(fairy["agilityscore"]), (0, 0, 0), font=titlefont)

    if len(arg) == 1:
        if arg[0] == "d":
            canvas = addFairydetaildstoImage(canvas)




    # save the current fairy with coutner reference
    canvas.save("Test Output/autogenfairy" + fairy['name'] + ".png")

    return


def printfairymontage(fairyies, columns):
    canvas2 = Image.new('RGBA', (columns * 800, ((len(fairyies) // columns) * 800) + 800),
                        (255, 255, 255, 255))  # Empty canvas colour (r,g,b,a)?
    y = 0
    while y < len(fairyies):
        im = getfairyimage(fairyies[y])
        canvas2.paste(im, ((y % columns) * 800, (y // columns) * 800), im)
        y += 1
    canvas2.show()
 #   canvas2.save("Test Output/fairymontage.png")
    return

def getfairymontage(fairyies, columns):
    number = int(len(fairyies))
    rows = number % columns
    if rows !=0:
        canvas2 = Image.new('RGBA', (columns * 800, ((len(fairyies) // columns) * 550) + 550),
                            (255, 255, 255, 255))  # Empty canvas colour (r,g,b,a)?
    else:
        canvas2 = Image.new('RGBA', (columns * 800, ((len(fairyies) // columns) * 550)),
                            (255, 255, 255, 255))  # Empty canvas colour (r,g,b,a)?
    y = 0
    while y < len(fairyies):
        # im = getfairyimage(fairyies[y])
        fairy = fairyies[y]
        name = fairy['name']
        im = getfairypicfromdb(name)
        im.paste = addFairyNametoImage(im, fairyies[y])
        canvas2.paste(im, ((y % columns) * 800, (y // columns) * 550), im)
        y += 1

    return canvas2


def printfairysheet(lower, upper):
# this takes a starting reference in the Database (lower) and prints out the next n (upper) fairies and produces a PNG file with 8 columns, suggest not more that 48 Fairies for A4

    fairies = []
    if (lower == 1):
        x=lower
        while (x<=lower+(upper*10)):
            fairies.append(get_fairy_from_db("FAIRY_TBL", x))
            x =x +10

    elif (lower % 10 != 1):
        x = int(((lower//10)*10)+1)
        while (x<=lower+(upper*10)):
            fairies.append(get_fairy_from_db("FAIRY_TBL", x))
            x =x +10

    elif (lower < 11):
        x = 11
        while (x<=lower+(upper*10)):
            fairies.append(get_fairy_from_db("FAIRY_TBL", x))
            x =x +10
    printfairymontage(fairies, 8)


def getrandomfairysheet(number):
# produces a 'number' of random fairies and retruns a canvas  PNG  with x columns, suggest not more that 48 Fairies for A4

    ids = []
    x=1
    totalfairies = int(numberoffairies('m') + numberoffairies('f'))
    while (x<=number):
        ids.append(random.randint(1, totalfairies))
        x=x+1

    fairies = get_multiple_fairies_from_db('FAIRY_TBL', ids)
    canvas = getfairymontage(fairies, 4)
    return canvas


def getfairysheet(number):
    # produces the first  'number' of fairies from the DB and retruns a canvas  PNG  with x columns, suggest not more that 48 Fairies for A4

    ids = []
    x = 1
    while (x <= number):
        ids.append(x)
        x = x + 1

    fairies = get_multiple_fairies_from_db('FAIRY_TBL', ids)
    canvas = getfairymontage(fairies, 4)
    return canvas


def addFairyNametoImage(Image, Fairy):
    canvas = Image
    fairy = Fairy
    draw = ImageDraw.Draw(canvas)
    titlefont = ImageFont.truetype("data/Arial.ttf", 30)
    draw.text((150, 500), fairy['name'], (0, 0, 0), font=titlefont)
    return canvas


def addFairyChartoImage(Image, Fairy):
    canvas = Image
    fairy = Fairy
    draw = ImageDraw.Draw(canvas)
    titlefont = ImageFont.truetype("data/Arial.ttf", 30)
    draw.text((450, 250), "Age Index :" + str(fairy['agescore']), (0, 0, 0), font=titlefont)
    draw.text((450, 280), "Kindness :" + str(int(fairy['kindscore'] / 2)), (0, 0, 0), font=titlefont)
    draw.text((450, 310), "Charactor :" + str(fairy['charactorscore']), (0, 0, 0), font=titlefont)
    draw.text((450, 340), "Magic Strength :" + str(fairy['magicscore']), (0, 0, 0), font=titlefont)
    draw.text((450, 370), "Agility :" + str(fairy["agilityscore"]), (0, 0, 0), font=titlefont)

    return canvas


def addFairydetaildstoImage(Image, Fairy):
    canvas = Image
    fairy = Fairy
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.truetype("data/Arial.ttf", 16)
    draw.text((475, 0), "Body ref: =" + str(fairy['bodyx']) + "," + str(fairy['bodyy']), (0, 0, 0), font=font)
    draw.text((475, 20), "Hair ref: =" + str(fairy['hairx']) + "," + str(fairy['hairy']), (0, 0, 0), font=font)
    draw.text((475, 40), "Wand ref: =" + str(fairy['wandx']) + "," + str(fairy['wandy']), (0, 0, 0), font=font)
    draw.text((475, 60), "Wings ref: =" + str(fairy['wingx']) + "," + str(fairy['wingy']), (0, 0, 0), font=font)
    draw.text((475, 80), "eyes ref: =" + str(fairy['eyesx']) + "," + str(fairy['eyesy']), (0, 0, 0), font=font)
    draw.text((475, 100), "mouth ref: =" + str(fairy['mouthsx']) + "," + str(fairy['mouthsy']), (0, 0, 0),
              font=font)
    draw.text((475, 120), "ears ref: =" + str(fairy['earsx']) + "," + str(fairy['earsy']), (0, 0, 0), font=font)
    draw.text((475, 140), "shoe ref: =" + str(fairy['shoesx']) + "," + str(fairy['shoesy']), (0, 0, 0),
              font=font)
    draw.text((475, 160), "access ref: =" + str(fairy['accessx']) + "," + str(fairy['accessy']), (0, 0, 0),
              font=font)
    draw.text((475, 180), "head access ref: =" + str(fairy['haccessx']) + "," + str(fairy['haccessy']),
              (0, 0, 0), font=font)
    draw.text((475, 200), "top clothes ref: =" + str(fairy['topx']) + "," + str(fairy['topy']), (0, 0, 0),
              font=font)
    draw.text((475, 220), "bottom clothes ref: =" + str(fairy['bottomx']) + "," + str(fairy['bottomy']),
              (0, 0, 0), font=font)

    return canvas

# todo save spritesheets in DB

def getfairypicfromdb(fairyname):
    if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
        con = pymysql.connect(
            host='104.197.55.21',
            unix_socket='testflask-1315:fairydb',
            user='root',
            passwd='TestFlask',
            database='My_Fairy_Kingdom',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)

    else:

        con = pymysql.connect(host='localhost',
                              user='dbuser',
                              passwd='TestFlask',
                              database='My_Fairy_Kingdom',
                              charset='utf8mb4',
                              cursorclass=pymysql.cursors.DictCursor)
    try:
        with con.cursor(pymysql.cursors.DictCursor) as cursor:
            # Read a single record
            sql = "SELECT * FROM FAIRY_TBL WHERE `fairyname`=%s"
            cursor.execute(sql, (fairyname,))
            result = cursor.fetchone()
            # if result == None :
            #         return None
            # desc = cursor.description
            # dict ={}

            # for(name,value) in zip(desc,result):
            #         dict[name[0]] =value

            imgstring = result['image']
            filelike = StringIO.StringIO(imgstring)
            canvas = Image.open(filelike)


    finally:
        con.close()

    return canvas


def getrandomfairypic():
    # gets a list of all fairy ID's in DB and randomly chooses one to draw to screen
    l = getfairyreferences("FAIRY_TBL")
    numgirl= (len(l[0]))
    numboy= (len(l[1]))
    Ids=[]
    for x in range(0,numgirl-1):
        Ids.append(l[0][x][0])
    for y in range(0,numboy-1):
        Ids.append(l[1][y][0])
    # fairy = get_fairy_from_db("FAIRY_TBL",int(Ids[random.randint(0,len(Ids))]) )
    # fairypicture = getrandomfairypic(int(Ids[random.randint(0,len(Ids))]))
    fairypicture = getrandomfairypic()
    return fairypicture


#   COMMAND LINE FUNCTIONS

def getrandomfairy():
    # gets a list of all fairy ID's in DB and randomly chooses one to draw to screen
    l = getfairyreferences("FAIRY_TBL")
    numgirl = (len(l[0]))
    numboy = (len(l[1]))
    Ids = []
    for x in range(0, numgirl - 1):
        Ids.append(l[0][x][0])
    for y in range(0, numboy - 1):
        Ids.append(l[1][y][0])
    fairy = get_fairy_from_db("FAIRY_TBL", int(Ids[random.randint(0, len(Ids))]))
    return fairy

def main(argv):
    #    for argv in sys.argv: 1
    #    print (argv)
    command = ''
    argument = ''
    try:
        opts, args = getopt.getopt(argv, "hf:g:c:d:ls:r:x")
    except getopt.GetoptError:
        print ('test.py -f <m/f> -g <DBref> -c <DB_Table_Name> -d <DB_TableName>  -l  -s <DBref>  -r -x')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('test.py -f <m/f> -g <DBref> -c <DB_Table_Name> -d <DB_TableName>  -l  -s <DBref>  -r -x')
            sys.exit()
        elif opt in ('-f'):
            #create Fairy
            fairy = (createfairy(arg))
            # do Fairy lookup to get ID number
            ID = str(getfairyIDfromname(fairy['name']))
            ID = int(ID[12:len(ID)-1])
            # get fairy object correspoding to returned ID
            fairy = get_fairy_from_db("FAIRY_TBL", ID)
            # Print to screen the created fairy details and the image
            print ('Fairy ' + fairy['name'] +' ID ' +str(ID) + ' has been created')
            getfairyimage(fairy).show()
            sys.exit()
        elif opt == '-l':
            list()
            sys.exit()
        elif opt in ('-s'):
            fairy = get_fairy_from_db("FAIRY_TBL", arg)
            print (fairy)
            getfairyimage(fairy).show()
            sys.exit()
        elif opt in ('-r'):
            resetDB(int(arg))
            sys.exit()
        elif opt =='-x':
            displayrandomfairypic()
            sys.exit()


def displayrandomfairypic():
    getrandomfairypic().show()


def resetDB(x):
# drops Fairy table and creates a new table with x number of random fairies
    delete_table("FAIRY_TBL")
    create_fairy_table("FAIRY_TBL")
for c in range(0, x):
    if (random.randint(0, 1) == 0):
        createfairy('m')
    else:
        createfairy('f')
return


def createrandomfairies(x):
    # creates with x number of random fairies and adds to DB

    for c in range (0,x):
        if (random.randint(0,1) ==0):
            createfairy('m')
        else: createfairy('f')
    return

def list():
#  List of Fairy References
    print ('There are ' + str(numberoffairies('all')) + ' fairies')
    print (str(numberoffairies('m')) + ' are male')
    print (str(numberoffairies('f')) + ' are female')
    print ('They are as follows:')
    print (getfairyreferences("FAIRY_TBL"))
    return


if __name__ == "__main__":
    main(sys.argv[1:])


#fairysheet(400,40)
#delete_table("FAIRY_TBL")
#create_fairy_table("FAIRY_TBL")
#createlotsfairies(10,"m")
#createlotsfairies(10,"f")

# p = personality()
# for key, value in p.iteritems():
#    print (key + " : " + str(value))
# createboyfairyfiles(10)
# createboyfairy("Piers Wilcox",1, 2, 0, 4, 2, 2, 7, 2, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0)
# creategirlfairyfiles(24)
# createfairy('f')   
# get_fairy_from_db(28) g
# create_fairy_table('test') c
# delete_table('FAIRY_TBL')
# create_fairy_table('FAIRY_TBL')
# createlotsfairies(50,"m")
# createlotsfairies(50,"f")
# print "Number of  girl fairies = "+str(numberoffairies('f'))
# print "Number of boy  fairies = "+str(numberoffairies('m'))
# print "Total number of fairies = "+str(numberoffairies('all'))
# fairy = get_fairy_from_db("FAIRY_TBL",1)
# fairypicture = getfairyimage(fairy)
# fairypicture.show()
# fairy = getrandomfairy()
# canvas = getfairypicfromdb(fairy['name'])
# canvas = Image.open(filelike)
# print(canvas)
# canvas.show()

# create a new canvas and loop through all the created fairy files and
# combine onto a single sheet, 10 * auto

# fairies = []
# x=1
# while (x<400):
  #    fairies.append(get_fairy_from_db("FAIRY_TBL", x))
    #  x =x +10 
# printfairymontage(fairies, 8)


# create_ssheet_table('Sprite')
#
from flask import *
import mysql.connector as mysql

# print("Hello World")

db = mysql.connect(
host ="localhost",
user = "raksha",
passwd = "Rakshamysql@123",
database = "Flight_booking")
cur = db.cursor()
app = Flask(__name__)

try:

    cur.execute('''CREATE TABLE IF NOT EXISTS Flights(id INTEGER PRIMARY KEY AUTO_INCREMENT, airline VARCHAR(100) NOT NULL, origin VARCHAR(100) NOT NULL, oricode VARCHAR(3), destination VARCHAR(100) NOT NULL, descode VARCHAR(3), duration VARCHAR(50), type VARCHAR(100), depdate DATE, economy INTEGER, business INTEGER);''')

    cur.execute('''CREATE TABLE IF NOT EXISTS Users(id INTEGER PRIMARY KEY AUTO_INCREMENT, firstName VARCHAR(100) NOT NULL, lastName VARCHAR(100) NOT NULL, userName VARCHAR(100) NOT NULL, email VARCHAR(100) NOT NULL, password VARCHAR(100) NOT NULL, phone VARCHAR(100) NOT NULL, address VARCHAR(100) NOT NULL, city VARCHAR(100) NOT NULL, state VARCHAR(100) NOT NULL, country VARCHAR(100) NOT NULL, sques VARCHAR(100) NOT NULL, sans VARCHAR(100) NOT NULL); ''')

    cur.execute('''CREATE TABLE IF NOT EXISTS Passengers(fid INTEGER ,pid INTEGER, fname VARCHAR(100), lname VARCHAR(100), FOREIGN KEY(fid) REFERENCES Flights(id), FOREIGN KEY(pid) REFERENCES Users(id));''')

except Exception as e:
    print("Table Already Exists: ", e)

print("Table Successfully created!!")


@app.route("/", methods=['POST','GET'])
def home():
    # global air, ori, orc, des, desco, ty, eco, bus
    cur.execute('SELECT id, origin, oricode, destination, descode FROM Flights;')
    flights = cur.fetchall()
    # print("------------------------------------")
    # print (flights)
    return render_template("home.html", flights=flights)



@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/help")
def help():
    return render_template("help.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")



@app.route('/ursignup', methods=['post', 'get'])
def ursignup():
    fname = str(request.form['person_fname'])
    lname = str(request.form['person_lname'])
    uname = str(request.form['person_username'])
    em = str(request.form['person_Email'])
    pwd = str(request.form['person_Password'])
    ph = str(request.form['person_Phone'])
    add = str(request.form['person_Address'])
    cit = str(request.form['person_City'])
    sta = str(request.form['person_State'])
    cou = str(request.form['person_Country'])
    sques = str(request.form['person_seqQues'])
    sans = str(request.form['person_seqAns'])

    cur.execute('''INSERT INTO Users(firstName, lastName, userName, email, password, phone, address, city, state, country, sques, sans) VALUES("''' + fname + '''","''' + lname + '''","''' + uname + '''","''' + em + '''","''' + pwd + '''","''' + ph + '''","''' + add + '''","''' + cit + '''","''' + sta + '''","''' + cou + '''","''' + sques + '''","''' + sans + '''"); ''')

    # cur.execute(f"INSERT INTO Users(firstName, lastName, userName, email, password, phone, address, city, state, country, sques, sans) VALUES ({fname}, {lname}, {uname}, {em}, {pwd}, {ph}, {add}, {cit}, {sta}, {cou}, {sques}, {sans});")

    db.commit()

    return jsonify(status=True)


@app.route("/checkLogin", methods=['post', 'get'])
def checkLogin():
    global uname, passwd
    uname = request.form['u_name']
    passwd = request.form['pass_wd']
    cur.execute('''SELECT userName, password FROM Users WHERE userName = "''' + uname + '''"; ''')

    string = cur.fetchone()
    print(string)
    unstring = string[0]
    pwdstring = string[1]


    if passwd == (pwdstring) and uname == (unstring):
        return jsonify(status=True)
    elif passwd == (pwdstring) and uname != (unstring):
        return jsonify(status = False, text= "Username is incorrect")
    elif passwd != (pwdstring) and uname == (unstring):
        return jsonify(status = False, text="Password is incorrect")
    else:
        return jsonify(status=False, text="Account does not exist")


    return jsonify(status=False)

@app.route("/profile", methods=['post', 'get'])
def profile():
    global uname, passwd
    # uname = request.form['u_name']
    cur.execute(''' SELECT firstName, lastName, userName, email, phone, address, city, state, country FROM Users WHERE userName = "''' + uname + '''"; ''')
    data = cur.fetchone()
    fn = data[0]
    ln = data[1]
    un = data[2]
    em = data[3]
    ph = data[4]
    ad = data[5]
    ci = data[6]
    st = data[7]
    co = data[8]
    print(data)

    return render_template("profile.html", fn = fn, ln = ln, un = un, em = em, ph = ph, ad = ad, ci = ci, st = st, co = co)


@app.route("/loginhome")
def loginhome():
    return render_template("loginhome.html")

@app.route("/logout")
def logout():
    return render_template("login.html")

@app.route("/booking")
def booking():
    cur.execute('SELECT id, origin, oricode, destination, descode FROM Flights;')
    flights = cur.fetchall()
    return render_template("booking.html", flights=flights)

@app.route("/booked", methods=["POST", "GET"])
def booked():
        global flight_id, fid, uname, passwd
        fid = str(request.form['vimaan'])

        cur.execute(''' SELECT * FROM Flights WHERE id = "''' + fid + '''"; ''')
        planes = cur.fetchone()
        print(planes)
        flight_id = planes[0]
        # flight_id = int(flid)
        airline = planes[1]
        origin = planes[2]
        orcode = planes[3]
        dest = planes[4]
        descode = planes[5]
        dur = planes[6]
        type = planes[7]
        # dat = str(planes[7])
        eco = planes[9]
        bus = planes[10]

        cur.execute(''' SELECT id, firstName, lastName FROM Users WHERE userName = "''' + uname + '''"; ''')
        data1 = cur.fetchone()
        print(data1)
        passid = data1[0]
        fname = data1[1]
        lname = data1[2]
        # passid = int(pid)
        cur.execute(''' INSERT INTO Passengers(fid, pid, fname, lname) VALUES ("''' + str(flight_id) + '''","''' + str(passid) + '''","''' + str(fname) + '''","''' + str(lname) + '''"); ''')

        db.commit()
        return jsonify(status=True)



if __name__ == "__main__":
    app.run(debug = True)






    # @app.route("/search", methods=['POST', 'GET'])
    # def search():
    #     global air, ori, orc, des, desco, ty, eco, bus
    #     search_flight = str(request.form['serfli'])
    #
    #     cur.execute(''' SELECT airline, origin, oricode, destination, descode, type, economy, business FROM Flights WHERE id = "''' + search_flight + '''"; ''')
    #     searchbox = cur.fetchone()
    #     air = searchbox[0]
    #     ori = searchbox[1]
    #     orc = searchbox[2]
    #     des = searchbox[3]
    #     desco = searchbox[4]
    #     ty = searchbox[5]
    #     eco = searchbox[6]
    #     bus = searchbox[7]
    #     print("Airline: ",air)
    #     print("Origin: ", ori)
    #     print("Destination: ", des)
    #     print("Type: ", ty)
    #     print("Economy:Rs.", eco)
    #     print("Business:Rs.", bus)
    #     return jsonify(status=True, text="Search Complete, Check Terminal")

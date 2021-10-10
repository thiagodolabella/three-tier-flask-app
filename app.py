from flask import Flask, render_template, request
from models import *
from random import randrange

folder_name="static"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://_YOUR_DB_USER_:_YOUR_DB_PASS_@_YOUR_DB_URL_:5432/_YOUR_DB_NAME_"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["TARGET_FOLDER"] = "images"
db.init_app(app)


def returnRandomImage():
    chooseNumberForImage = randrange(0, 9)
    if chooseNumberForImage == 0:
        return "fake-person-01.jpg"
    elif chooseNumberForImage == 1:
        return "fake-person-02.jpg"
    elif chooseNumberForImage == 2:
        return "fake-person-03.jpg"
    elif chooseNumberForImage == 3:
        return "fake-person-04.jpg"
    elif chooseNumberForImage == 4:
        return "fake-person-05.jpg"
    elif chooseNumberForImage == 5:
        return "fake-person-06.jpg"
    elif chooseNumberForImage == 6:
        return "fake-person-07.jpg"
    elif chooseNumberForImage == 7:
        return "fake-person-08.jpg"
    elif chooseNumberForImage == 8:
        return "fake-person-09.jpg"
    elif chooseNumberForImage == 9:
        return "fake-person-10.jpg"
    else: return "fake-person-01.jpg"


@app.route('/')
@app.route("/", methods=["GET"])
def index():
    contList=Contacts.query.all()
    cont=Contacts.query.first()
    return render_template("index.html", cont=cont, contList=contList)
    
@app.route("/", methods=["POST"])
def addcontact():
    conid=0
    #store values recieved from HTML form in local variables
    fName=request.form.get("FirstName")
    lName=request.form.get("LastName")
    workCompany=request.form.get("WorkCompany")
    jobTitle=request.form.get("WorkJobTitle")
    mobile=request.form.get("Mobile")
    email=request.form.get("email")
    displayPhoto=returnRandomImage()
    #Pass on the local values to the corresponfding model
    contact = Contacts( fName=fName, lName=lName,workCompany=workCompany, jobTitle=jobTitle,mobile=mobile,email=email,displayPhoto=displayPhoto)
    db.session.add(contact)
    db.session.commit()
    cont=conid
    contList=Contacts.query.all()
    return render_template("index.html", cont=cont, contList=contList) 
    
@app.route("/showContact/<int:conid>")
def showContact(conid):
    # select row from contacts table for contact ID passed from main page
    cont=Contacts.query.filter_by(contactID=conid).first()
    return render_template("contact.html",cont=cont)
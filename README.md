# Simple 3 Tier Contact Form App

### Prerequsites:
* Python 3.8 installed
* IDE / Text Editor of your choosing
* Terminal / Command Prompt / Powershell
* Postgre instance (am using 13.3)

### To install:
* If using AWS EC2 the following commands will help get started first (not needed when developing locally):
``` bash
sudo yum install postgresql-devel && sudo yum install git
```

* Download this repository and navigate to the downloaded project folder within your terminal of choice.
``` bash
git clone https://github.com/MattJColes/three-tier-flask-app.git && cd three-tier-flask-app
```

* Create a virtual environment within your project folder:
``` bash
python3 -m venv venv

source ./venv/bin/activate
// OR FOR WINDOWS
.\venv\Scripts\activate
```

* Install any extra dependancies (note again Mac you'll need to use pip3 instead):
``` bash
pip3 install -r requirements.txt
```

* Provision the database tables within your Postgres instance by running the following within your SQL editor:
``` bash
CREATE TABLE contacts
(
    "contactID" SERIAL,
    "fName" character varying(30) COLLATE pg_catalog."default" NOT NULL,
    "lName" character varying(30) COLLATE pg_catalog."default",
    "workCompany" character varying(50) COLLATE pg_catalog."default",
    mobile character varying(20) COLLATE pg_catalog."default",
    email character varying(50) COLLATE pg_catalog."default",
    "jobTitle" character varying(50) COLLATE pg_catalog."default",
    "displayPhoto" character varying(50) COLLATE pg_catalog."default",
    CONSTRAINT contacts_pkey PRIMARY KEY ("contactID")
)
```

* Within app.py update the following string (on line 7) with your postgres database details:
``` bash
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://_YOUR_DB_USER_:_YOUR_DB_PASS_@_YOUR_DB_URL_:5432/_YOUR_DB_NAME_"
```

### Now you can run locally
* Run the following command in terminal to run the app on port 8080: 
``` bash
python3 wsgi.py
```
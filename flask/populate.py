import json
import sqlite3
from peewee import *
from models import db, Aircraft


JSON_FILE = "global.json"
DB_FILE = "items.db"

json = json.load(open(JSON_FILE))
conn = sqlite3.connect(DB_FILE)

c = conn.cursor()
c.execute('create table Aircraft (id integer primary key AUTOINCREMENT, operator, model, registration, cn_fl)')

for i in range(len(json)):
	operator = json[i]["operator"]
	model = json[i]["model"]
	registration = json[i]["registration"]
	cn_fl = json[i]["cn_fl"]

	Aircraft.create(id=i, operator=operator, model=model, registration=registration, cn_fl=cn_fl)

conn.commit()
c.close()
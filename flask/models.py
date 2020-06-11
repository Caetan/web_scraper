#!/usr/bin/env python
from peewee import (SqliteDatabase, Model, IntegerField, TextField)


db = SqliteDatabase('items.db')

class Aircraft(Model):
	id = IntegerField()
	operator = TextField()
	model = TextField()
	registration = TextField()
	cn_fl = TextField()

	class Meta:
		database = db

if __name__ == '__main__':
    db.connect()
    db.create_tables([Aircraft])

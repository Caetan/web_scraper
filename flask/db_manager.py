#!/usr/bin/env python
from peewee import *
from models import db, Aircraft


def create_obj(operator,model,registration,cn_fl):
	"""
	Creating objects
	"""
	Aircraft.create(operator=operator, model=model, registration=registration, cn_fl=cn_fl)


def retrive_obj(mode, iden, search):
	# """
	# Retrieving objects
	# """

	# Getting a single instance:
	if (mode == 1):
		aircraft = Aircraft.get(Aircraft.id == iden)
		#print(aircraft)
		return aircraft


	if (mode == 2):
	# Getting all instances:
		aircrafts = Aircraft.select()
		#for aircraft in aircrafts:
			#print(aircraft.operator)
		return aircrafts

	if (mode == 3):
		aircrafts = Aircraft.select().where(Aircraft.operator.contains(search))
		return aircrafts
	

def update_obj(iden, operator, model, registration, cn_fl):
	"""
	Updating objects
	"""
	aircraft = Aircraft.get(Aircraft.id == iden)
	aircraft.operator = operator
	aircraft.model = model
	aircraft.registration = registration
	aircraft.cn_fl = cn_fl
	aircraft.save()

def delete_obj(iden):
	"""
	Deleting objects
	"""
	# Remove a single instance
	xps = Aircraft.get(Aircraft.id == iden)
	xps.delete_instance()

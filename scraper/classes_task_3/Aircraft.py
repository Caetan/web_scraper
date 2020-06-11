#!/usr/bin/env python
import sys
import json
import os


###########################
# Class 1: Aircraft
###########################

class Aircraft:
	def __init__(self, operator, model, registration, cn_fl):
		self.operator = operator
		self.model = model
		self.registration = registration
		self.cn_fl = cn_fl


	def check_unknown_fields(self):
		for attr, value in self.__dict__.items():
			# To check if CN or FL is known
			field = value
			if (value.find('/') != -1):
				field = value.split("/")
			for f in field:
				if(f == "?"):
					value = value.replace('?', "UNKNOWN")
					setattr(self, attr, value)

	def to_string(self):
		self.check_unknown_fields()
		print("\nAIRCRAFT INFO:")
		print("Flight operator:", self.operator)
		print("Flight model:", self.model)
		print("Flight registration:", self.registration)
		print("CN/FL:", self.cn_fl)

	# To get the operator type (Military, Taxi, none (by default commercial), etc) from Operator field
	def get_type(self):
		# Check those which only have COMPANY and non type (by default non type refears to Commercial flights)
		if (self.operator.find(' - ') != -1):
			type_company = self.operator.split(" - ")
			f_type = type_company[0]
		else:
			f_type = "Commercial" # value by default

		return f_type

	# To get the operator type (Military, Taxi, none (by default commercial), etc) from Operator field
	def get_company(self):
		# Check those which only have COMPANY and non type (by default non type refears to Commercial flights)
		if (self.operator.find(' - ') != -1):
			type_company = self.operator.split(" - ")
			company = type_company[1]
		else:
			company = self.operator

		return company


	def get_cn(self):
		cn = self.cn_fl
		# Checking if there are any
		if (self.cn_fl.find('/') != -1):
			cn_fl = self.cn_fl.split("/")
			cn = cn_fl[0]
		print("Construction number:", cn)

		return cn

	def get_fl(self):
		fl = self.cn_fl
		# Checking if there are any
		if (self.cn_fl.find('/') != -1):
			cn_fl = self.cn_fl.split("/")
			fl = cn_fl[1]
		print("Fuselage:", fl)

		return fl


###########################
# Persistence Layer
###########################

def obj_to_json(self):
	if not os.path.exists('./JSON/'):
		os.makedirs('./JSON/')
	with open("./JSON/"+self.__class__.__name__+str(id(self))+".json", "a+") as file:
		json.dump(vars(self), file, indent=4)

def json_to_obj(self, mode):
	if mode == 1:
		loc = "./JSON/"+self.__class__.__name__+str(id(self))+".json"
	else: # Manual object'a ID typing
		loc = "./JSON/"+self+".json"
	
	with open(loc) as file:
	    my_obj = json.load(file)
	
	print(my_obj)
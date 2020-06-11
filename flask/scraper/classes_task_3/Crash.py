#!/usr/bin/env python
import sys
import json
import os

###########################
# Class 2: Crash
###########################

class Crash:
    def __init__(self, operator, location, flight_num):
    	self.company = operator.get_company()
    	self.location = location
    	self.flight_num = flight_num


    def check_unknown_fields(self):
    	for attr, value in self.__dict__.items():
    		# To check if anyone is known
    		field = value.split("/")
    		for f in field:
	    		if(f == "?"):
	    			setattr(self, attr, "UNKNOWN")

    def to_string(self, operator):
        self.check_unknown_fields()
        operator.check_unknown_fields()
        print("\nCRASH INFO:")
        print("Company:", self.company)
        print("Type:", operator.get_type())
        print("Flight number #:", self.flight_num)
        print("Location:", self.location)

    def get_company(self):
        return self._company

    def set_company(self, value):
        self._company = value

    def delete_company(self):
        del self._company

    def get_location(self):
        return self._location

    def set_location(self, value):
        self._location = value

    def delete_location(self):
        del self._location

    location = property(get_location, set_location, delete_location)
    company = property(get_company, set_company, delete_company)



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
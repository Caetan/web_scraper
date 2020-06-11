#!/usr/bin/env python
import sys
import json

# python3 task2.py


###########################
# Class 1: Aircraft
###########################

class Aircraft:
	def __init__(self, operator, model, registration, cn_fl):
		self.operator = operator
		self.model = model
		self.registration = registration
		self.cn_fl = cn_fl

	def to_string(self):
		print("\nAIRCRAFT INFO:")
		print("Flight operator:", self.operator)
		print("Flight model:", self.model)
		print("Flight registration:", self.registration)
		print("CN/FL:", self.cn_fl)

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

	# To get the operator type (Military, Taxi, none (by default commercial), etc) from Operator field
	def get_type(self):
		# Check those which only have COMPANY and non type (by default non type refears to Commercial flights)
		if (self.operator.find('-') != -1):
			type_company = self.operator.split(" - ")
			f_type = type_company[0]
		else:
			f_type = "Commercial" # value by default

		return f_type

	# To get the operator type (Military, Taxi, none (by default commercial), etc) from Operator field
	def get_company(self):
		# Check those which only have COMPANY and non type (by default non type refears to Commercial flights)
		if (self.operator.find('-') != -1):
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
# Class 2: Crash
###########################

class Crash:
    def __init__(self, operator, location, flight_num):
    	self.company = operator.get_company()
    	self.location = location
    	self.flight_num = flight_num

    def to_string(self, operator):
    	print("\nCRASH INFO:")
    	print("Company:", self.company)
    	print("Type:", operator.get_type())
    	print("Flight number #:", self.flight_num)
    	print("Location:", self.location)

    def check_unknown_fields(self):
    	for attr, value in self.__dict__.items():
    		# To check if anyone is known
    		field = value.split("/")
    		for f in field:
	    		if(f == "?"):
	    			setattr(self, attr, "UNKNOWN")

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
# Class 3: Victims
###########################

class Victims:
	def __init__(self, crash, aboard, fatalities, ground):
		self.aboard = aboard
		self.fatalities = fatalities
		self.ground = ground

	def to_string(self, crash):
		print("\nVICTIMS INFO:")
		print("Company: ", crash.get_company())
		print("Location: ", crash.get_location())
		print("Aboard: ", self.aboard)
		print("Fatalities: ", self.fatalities)
		print("Ground: ", self.ground)

	def check_unknown_fields(self):
		for attr, value in self.__dict__.items():
			# To check if anyone is known
			field = value.split("/")
			for f in field:
				if(f == "?"):
					setattr(self, attr, "UNKNOWN")


	# To separate passengers and crew victims
	def victims_role(self):
		try:
			aboard = self.aboard.replace('?', "UNKNOWN").replace('(','').replace(')','').split(" ")
			total_aboard = aboard[0]
			passangers_aboard = aboard[1].split(":")[1]
			crew_aboard = aboard[2].split(":")[1]
			print("There were", total_aboard, "people aboard,", passangers_aboard, "were passangers and", crew_aboard, "were crew")
			fatalities = self.fatalities.replace('?', "UNKNOWN").replace('(','').replace(')','').split(" ")
			total_fatalities = fatalities[0]
			passangers_fatalities = fatalities[1].split(":")[1]
			crew_fatalities = fatalities[2].split(":")[1]
			print("There were", total_fatalities, "fatalities,", passangers_fatalities, "were passangers and", crew_fatalities, "were crew")
			print("There were", self.ground.replace('?', "UNKNOWN"), "deads in the ground")

			return total_aboard, passangers_aboard, crew_aboard, total_fatalities, passangers_fatalities, crew_fatalities, self.ground
		except:
			print("There is an UNKNOWN number of victims")

			return None

	def alive_passengers(self):
		try:
			aboard = self.aboard.replace('(','').replace(')','').split(" ")
			passangers_aboard = aboard[1].split(":")[1]
			fatalities = self.fatalities.replace('(','').replace(')','').split(" ")			
			passangers_fatalities = fatalities[1].split(":")[1]
			if ((passangers_aboard.find('?') == -1) or (passangers_fatalities.find('?') == -1)):
				print("There were", (int(passangers_aboard) - int(passangers_fatalities)), "passengers alive")
				return (int(passangers_aboard) - int(passangers_fatalities))
			else:
				print("There is an UNKNOWN number of passenger victims")
				return None
		except:
			print("There is an UNKNOWN number of passenger victims")

			return None

	def alive_crew(self):
		try:
			aboard = self.aboard.replace('(','').replace(')','').split(" ")
			crew_aboard = aboard[2].split(":")[1]
			fatalities = self.fatalities.replace('(','').replace(')','').split(" ")
			crew_fatalities = fatalities[2].split(":")[1]
			if (crew_aboard.find('?') == -1) or (crew_fatalities.find('?') == -1):
				print("There were", (int(crew_aboard) - int(crew_fatalities)), "crew alive")
				return (int(crew_aboard) - int(crew_fatalities))
			else:
				print("There is an UNKNOWN number of crew victims")
				return None
		except:
			print("There is an UNKNOWN number of crew victims")

			return None


# ###########################
# # Class 4: Route
# ###########################

# class Route:
# 	def __init__(self, origin, destination):
# 		# Añadir objeto Crash para interactuación entre clases
# 		self.origin = origin
# 		self.destination = destination

# 	def to_string(self):
# 		print("The origin was " + self.origin)
# 		print("The destination was " + self.origin)

# 	# To get location and country origin
# 	def get_origin(origin):

# 	# To get location and country destination
# 	def get_destination(destination):



###########################
# Persistence Layer
###########################

def obj_to_json(self):
	with open("JSON/"+self.__class__.__name__+str(id(self))+".json", "a+") as file:
		json.dump(vars(self), file, indent=4)

def json_to_obj(self, mode):
	if mode == 1:
		loc = "JSON/"+self.__class__.__name__+str(id(self))+".json"
	else:
		loc = "JSON/"+self+".json"
	
	with open(loc) as file:
	    my_obj = json.load(file)
	
	print(my_obj)


# a1 = Aircraft("Spanair", "McDonnell Douglas MD-82", "EC-HFP", "53148/2072")
# a2 = Aircraft("?", "?", "?", "?/2072")
# c1 = Crash(a1, "West Germany", "5022")
# c2 = Crash(a1, "?", "?")
# v1 = Victims(c1, "35 (passengers:30 crew:5)", "76 (passengers:70 crew:6)", "3")
# v2 = Victims(c1, "35 (passengers:? crew:5)", "76 (passengers:70 crew:?)", "3")
# v3 = Victims(c1, "? (passengers:? crew:5)", "76 (passengers:? crew:?)", "?")
# v4 = Victims(c2, "?", "?", "?")

# obj_to_json(a1)
# obj_to_json(a2)
# obj_to_json(c1)
# obj_to_json(c2)
# obj_to_json(v1)
# obj_to_json(v2)
# obj_to_json(v3)
# obj_to_json(v4)


# json_to_obj(a1, 1)
# json_to_obj("Aircraft4387530928", 2)
# json_to_obj(a2, 1)
# json_to_obj(c1, 1)
# json_to_obj(c2, 1)
# json_to_obj(v1, 1)
# json_to_obj(v2, 1)
# json_to_obj(v3, 1)
# json_to_obj(v4, 1)


# # TEST 1 - Class 1: Aircraft 
# a1 = Aircraft("Spanair", "McDonnell Douglas MD-82", "EC-HFP", "53148/2072")
# a1.check_unknown_fields()
# a1.to_string()
# a1.get_type()
# a1.get_company()
# a1.get_cn()
# a1.get_fl()

# # TEST 2 - Class 1: Aircraft 
# a2 = Aircraft("?", "?", "?", "?/2072")
# a2.check_unknown_fields()
# a2.to_string()
# a2.get_type()
# a2.get_company()
# a2.get_cn()
# a2.get_fl()

# #----------------------------------
# # TEST 3 - Class 2: Crash 
# c1 = Crash(a1, "West Germany", "5022")
# c1.check_unknown_fields()
# c1.to_string(a1)

# # TEST 4 - Class 2: Crash 
# c2 = Crash(a1, "?", "?")
# c2.check_unknown_fields()
# c2.to_string(a1)

# #----------------------------------
# # TEST 5 - Class 3: Victims 
# v1 = Victims(c1, "76 (passengers:60 crew:16)", "30 (passengers:15 crew:15)", "3")
# v1.check_unknown_fields()
# v1.to_string(c1)
# v1.victims_role()
# v1.alive_passengers()
# v1.alive_crew()

# # TEST 6 - Class 3: Victims 
# v2 = Victims(c1, "76 (passengers:? crew:16)", "30 (passengers:15 crew:?)", "3")
# v2.check_unknown_fields()
# v2.to_string(c1)
# v2.victims_role()
# v2.alive_passengers()
# v2.alive_crew()

# # TEST 7 - Class 3: Victims 
# v3 = Victims(c1, "? (passengers:? crew:5)", "30 (passengers:? crew:?)", "?")
# v3.check_unknown_fields()
# v3.to_string(c1)
# v3.victims_role()
# v3.alive_passengers()
# v3.alive_crew()

# # TEST 8 - Class 3: Victims 
# v4 = Victims(c2, "?", "?", "?")
# v4.check_unknown_fields()
# v4.to_string(c2)
# v4.victims_role()
# v4.alive_passengers()
# v4.alive_crew()

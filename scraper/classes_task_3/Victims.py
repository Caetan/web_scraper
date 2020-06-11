#!/usr/bin/env python
import sys
import json
import os


###########################
# Class 3: Victims
###########################

class Victims:
	def __init__(self, crash, aboard, fatalities, ground):
		self.aboard = aboard
		self.fatalities = fatalities
		self.ground = ground


	def check_unknown_fields(self):
		for attr, value in self.__dict__.items():
			# To check if anyone is known
			field = value.split("/")
			for f in field:
				if(f == "?"):
					setattr(self, attr, "UNKNOWN")

	def to_string(self, crash):
		self.check_unknown_fields()
		crash.check_unknown_fields()
		print("\nVICTIMS INFO:")
		print("Company: ", crash.get_company())
		print("Location: ", crash.get_location())
		print("Aboard: ", self.aboard)
		print("Fatalities: ", self.fatalities)
		print("Ground: ", self.ground)

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
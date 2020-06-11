import random
import re
import sys
import time
import re
import bs4
import requests
from bs4 import BeautifulSoup
from threading import Thread, Lock
import threading
from classes_task_3 import Aircraft, Crash, Victims

def get_accident_info(accident_dict, lock):
	print("\n\033[1;32;10m THREAD GETTER ID ", threading.get_ident(), "\033[0m\n")
	lock.acquire()
	date = accident_dict.get('Date:')
	time = accident_dict.get('Time:')
	location = accident_dict.get('Location:')
	operator = accident_dict.get('Operator:')
	flight_num = accident_dict.get('Flight #:')
	route = accident_dict.get('Route:')
	model = accident_dict.get('AC\n        Type:')
	registration = accident_dict.get('Registration:')
	cn_ln = accident_dict.get('cn / ln:')
	aboard = accident_dict.get('Aboard:')
	fatalities = accident_dict.get('Fatalities:')
	ground = accident_dict.get('Ground:')
	summary = accident_dict.get('Summary:')
	lock.release()
	#print(accident_dict)
	#print(date, time, location, operator, flight_num, route, model, registration, cn_ln, aboard, ground, summary)
	#print("\n")
	print("\n*********************************************")
	print("*********************************")
	print("* ACCIDENT in " + date + " *")
	print("*********************************")
	get_info_aircraft(operator, model, registration, cn_ln)
	get_info_crash(location, operator, model, flight_num, cn_ln)
	get_info_victims(location, operator, flight_num, model, registration, cn_ln, aboard, fatalities, ground)
	print("\n*********************************************\n")


def get_info_aircraft(operator, model, registration, cn_ln):
	a1 = Aircraft.Aircraft(operator, model, registration, cn_ln)
	a1.to_string()
	a1.get_type()
	a1.get_company()
	a1.get_cn()
	a1.get_fl()
	print("\n\t\033[1;32;40m Writing object in a file\033[0m\n")
	Aircraft.obj_to_json(a1)
	#Aircraft.json_to_obj(a1, 1)
	#Aircraft.json_to_obj("Aircraft4387530928", 2)


def get_info_crash(location, operator, model, flight_num, cn_ln):
	a1 = Aircraft.Aircraft(operator, model, flight_num, cn_ln)
	c1 = Crash.Crash(a1, location, flight_num)
	c1.to_string(a1)
	print("\n\t\033[1;32;40m Writing object in a file\033[0m\n")
	Crash.obj_to_json(c1)
	#Crash.json_to_obj(c1, 1)
	#Crash.json_to_obj("Crash4387530928", 2)


def get_info_victims(location, operator, flight_num, model, registration, cn_ln, aboard, fatalities, ground):
	a1 = Aircraft.Aircraft(operator, model, registration, cn_ln)
	c1 = Crash.Crash(a1, location, flight_num)
	v1 = Victims.Victims(c1, aboard, fatalities,ground)
	v1.to_string(c1)
	v1.victims_role()
	v1.alive_passengers()
	v1.alive_crew()
	print("\n\t\033[1;32;40m Writing object in a file\033[0m\n")
	Victims.obj_to_json(v1)
	#Victims.json_to_obj(v1, 1)
	#Victims.json_to_obj("Victims4387530928", 2)


def parser(init_time, accident_dict, page_soup, lock, n_obj):
	count = 1
	# Looping all URL to years
	for block in page_soup.find_all('tr'):
		for link in block.find_all('a'):
			year_url = base_url + link.get('href')
			year = link.get('href').split("/")[1]
			if (year == "1929.htm"):  # Due to the webpage has the URL without
				year_url = base_url + '/' + link.get('href')
			response_year = requests.get(year_url)
			page_soup_year = BeautifulSoup(response_year.text, 'html.parser')
			# Looping all accidents from an specific year
			for block_year in page_soup_year.find_all('td'):
				for link_year in block_year.find_all('a'):
					accident_url = base_url + '/' + year + '/' + link_year.get('href')
					response_accident = requests.get(accident_url)
					page_soup_accident = BeautifulSoup(response_accident.text, 'html.parser')
					# Looping info from each accident
					for block_accident in page_soup_accident.find_all('tr'):
						# Take the first td with the name of the field
						for accident in block_accident.find('td'):
							index = accident.text
						# Take the second td with the content of the field
						for accident2 in block_accident.find_all('td'):
							content = re.sub(' +', ' ', accident2.text.replace(u'\xa0', u' ')) # Removing \xa0 character and multiple spaces
						lock.acquire()
						accident_dict[index] = content
						lock.release()
					print("\n\033[1;32;10m THREAD PARSER ID ", threading.get_ident(), "\033[0m\n")
					p2 = Thread(target=get_accident_info, args=(accident_dict, lock))
					p2.start()
					p2.join()
					print("TOTAL OBJECTS PARSED", count)
					count = count + 1
					if (count == (n_obj + 1)):
						return
					end_time = time.perf_counter()
					print("\n\nPARTIAL TIME:" , end_time - init_time)


if (__name__ == '__main__'):
	lock = Lock()
	init_time = time.perf_counter()
	accident_dict = {}
	n_obj = 100

	base_url = 'http://www.planecrashinfo.com'
	db_url = '/database.htm'

	response = requests.get(base_url + db_url)

	if (response.status_code != 200):
		print("Error accesing webpage")
		exit()

	page_soup = BeautifulSoup(response.text, 'html.parser')

	p1 = Thread(target=parser, args=(init_time, accident_dict, page_soup, lock, n_obj))
	p1.start()
	p1.join()

	end_time = time.perf_counter()
	print("\n\nTOTAL TIME:" , end_time - init_time)
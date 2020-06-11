import json
import os

ind = 0
f1data = ""

with open ('../global.json', 'w+') as f3:
	f3.write("[\n")
 
for root, dirs, files in os.walk("JSON"):
	file_count = len(files)
	for file in files:
		ind = ind + 1
		if file.endswith('.json'):
			with open("JSON/"+file) as f1:
				f1data = f1.read()
			# 	if (ind == (file_count)):
			# 		f1data = f1data[:6]+"\"id\": " + str(ind) + ",\n\t"+f1data[6:]+"\n"					
			# 	else:
			# 		f1data = f1data[:6]+"\"id\": " + str(ind) + ",\n\t"+f1data[6:]+",\n"
			with open ('../global.json', 'a') as f3:
				if (ind == 1):
					f3.write("\n\t"+f1data)					
				else:
					f3.write(",\n\t"+f1data)			
				

with open ('../global.json', 'a') as f3:
	f3.write("\n]")

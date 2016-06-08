import csv
import json
import itertools

#Program for changing the CSV file to json file for a list of web pages to be tested
#TODO Some ptoblem for the format of the json file, need to change the [ to { in some places mannuelly
class CsvToJson():
	def __init__(self):
		self.CSV=csv.reader(open('pages.csv','rb'))
		self.sites=[]

	def getJson(self, number):
		print "Generate a json list of pages"		
		f= open('test_pages.json','w')
		data=[{"description":"Pages to be tested Attention: URL needs to be begun with http or https to make the test succeed"}]
		for item in itertools.islice(self.CSV, 0, number):
                        self.sites.append({"url": item[1]})

		data.append({"pages":[self.sites]})
		out=json.dumps(data,indent=4, sort_keys=True)
		f.write(out)




try1=CsvToJson()
try1.getJson(50)

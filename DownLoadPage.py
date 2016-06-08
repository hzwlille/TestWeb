import os
import json
	

class DownLoadPage():

	def __init__(self):
		print "Download web pages in local files"
		self.pageList = []
		self.files = "sites" #file in which we will put the site
		self.pageDownloaded = []

	def setPageListFromJson(self, jFile):
        #From json file, import pages to download
	        with open(jFile) as json_pages:
        		allPages=json.load(json_pages)
              		json_pages.close()
                	for page in allPages['pages']:
                        	self.pageList.append(page['url'])
       		print "Pages loaded from Json file\n"
        	self.printPageList()


	def downLoadUrl(self,url):
		command=self.files+' '+url
		os.system('wget -E -H -k -K -p -P %s'%command)
		self.pageDownloaded.append(url)
	
	def downLoadWithTimeout(self,url, time):
	#This is perhaps not working, to be cheked
                command=self.files+' '+url
                monitor(os.system('wget -E -H -k -K -p -P %s'%command),30)
	

	def downAllUrls(self):
		for url in self.pageList:
			self.downLoadUrl(url)


	def printPageList(self):
        	for page in self.pageList:
                	print page

        def printPageLoad(self):
		print "Pages loaded are:"
                for page in self.pageDownloaded:
                        print page






try1=DownLoadPage()
try1.setPageListFromJson("test_pages.json")	
try1.downAllUrls()
try1.printPageLoad()

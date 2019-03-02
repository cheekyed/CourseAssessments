from urllib.request import urlopen
import sys
import socket 
from bs4 import BeautifulSoup

courseUrlList = []
tableRows = []
maintenanceUrl = "http://maintenance.business.unsw.edu.au/#assessment"


def addUrls():
	for i in range (1,len(sys.argv)):
		courseUrl = 'https://www.business.unsw.edu.au/degrees-courses/course-outlines/archives/' + sys.argv[i] + '#assessment'
		courseUrlList.append(courseUrl)
		print(courseUrlList)
		return

def internet_on():
	try:
		socket.create_connection(("www.google.com", 80))
		print('internet connection is on')
	except OSError:
		print('no internet connection')
		sys.exit()
	return

def getAssessmentData():
	for url in courseUrlList:
		counter = 1
		page = urlopen(url)
		if page.geturl() == maintenanceUrl:
			print('page is under maintenance')
			sys.exit()
		else:
			pageHtml = BeautifulSoup(page, 'html.parser')
			print(sys.argv[counter] + ' html successfully acquired')
			counter +=1 
			table = pageHtml.find('table', attrs={'id' : 'assessment-table'})
			table_body = table.find('tbody')
			rows = table_body.find_all('tr')
			for row in rows:
				elementTags = row.find_all(['td','th'])
				elementsList = []
				for ele in elementTags:
					if ele.text.strip() != 'Length' or ele.text.strip() == '-':
						elementsList.append(ele.text.strip())
						print(ele.text.strip())	
				print('=========')
				tableRows.append(elementsList)
			print(tableRows)
		return

def file_ouput():

	 return

def main ():
	addUrls()
	internet_on()
	getAssessmentData()
 	




if __name__ == '__main__':
	main()


from urllib.request import urlopen
import sys
import socket 
from bs4 import BeautifulSoup

courseUrlList = []
pageHtmlList = []
maintenanceUrl = "http://maintenance.business.unsw.edu.au/#assessment"


def addUrls():
	for i in range (1,len(sys.argv)):
		courseUrl = 'https://www.business.unsw.edu.au/degrees-courses/course-outlines/archives/' + sys.argv[i] + '#assessment'
		courseUrlList.append(courseUrl)
		return

def internet_on():
	try:
		socket.create_connection(("www.google.com", 80))
		print('internet connection is on')
	except OSError:
		print('no internet connection')
		sys.exit()
	return

def getHtml():
	for url in courseUrlList:
		page = urlopen(url)
		if page.geturl() == maintenanceUrl:
			print('page is under maintenance')
			sys.exit()
		else:
			pageHtml = BeautifulSoup(page, 'html.parser')
			pageHtmlList.append(pageHtml)
		print('page html successfully acquired')
		return

def main ():
	addUrls()
	internet_on()
	getHtml()
 




if __name__ == '__main__':
	main()

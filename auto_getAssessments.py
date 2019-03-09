from urllib.request import urlopen
import os
import sys
import socket 
import csv
from bs4 import BeautifulSoup
from pathlib import Path

courseUrlList = []
tableList = []
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
		print('internet connection is on\n')
	except OSError:
		print('no internet connection\n')
		sys.exit()
	return

def getAssessmentData():
	counter = 1
	for url in courseUrlList:
		page = urlopen(url)
		if page.geturl() == maintenanceUrl:
			print('page is under maintenance')
			sys.exit()
		else:
			pageHtml = BeautifulSoup(page, 'html.parser')
			print(sys.argv[counter] + ' html successfully acquired\n')
			counter +=1 
			table = pageHtml.find('table', attrs={'id' : 'assessment-table'})
			table_body = table.find('tbody')
			rows = table_body.find_all('tr')
			tableRows = []
			for row in rows:
				elementTags = row.find_all(['td','th'] )
				elementsList = []
				for ele in elementTags:
					if  ele.get('data-th') != 'Length':
						if ele.text.strip() != 'Length':
							elementsList.append(ele.text.strip())
							print(ele.text.strip())	
				print('=========')
				tableRows.append(elementsList)
			tableList.append(tableRows)
			print('\n')
	print(tableList)
	return

def file_ouput():
	i =0
	fileName = 'Assessments.csv'
	try:
		if os.path.isfile(fileName):
			os.remove(fileName)
			print(fileName + ' removed')
		f = open(fileName,'w', newline = '')
	except:
		print('Assessments.csv is already open. need to close before writing and removing')
		sys.exit()
		
	writer = csv.writer(f)
	for tables in tableList:
		i+=1
		writer.writerow([sys.argv[i]])
		for rows in tables:
			writer.writerow(rows)
		writer.writerow('')
	f.close()
	print('csv file sucessfully created')
	return

def main ():
	addUrls()
	internet_on()
	getAssessmentData()
	file_ouput()




if __name__ == '__main__':
	main()


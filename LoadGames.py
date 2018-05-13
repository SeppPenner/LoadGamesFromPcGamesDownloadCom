import requests
from bs4 import BeautifulSoup
import sys
import datetime

mainPageUrl = 'https://pcgames-download.com/'
mainFilePath = './loading/mainPage.html'
pagePath = './loading/'

def loadGameData():
	"Loads computer games data"
	print ('Loading number of pages')
	response = requests.get(mainPageUrl)
	with open(mainFilePath, 'wb') as f:
		f.write(response.content)
	soup = BeautifulSoup(open(mainFilePath, encoding="utf8"), 'html.parser')
	for lastPage in soup.find_all(class_='last'):
		lastPageText = lastPage.get('href').strip()
		lastPageNumber = getLastPageNumber(lastPageText)
		print ('Last available page: ' + lastPageText)
		continue
	data = []
	for currentPageNumber in range(1, lastPageNumber + 1):
		print('Loading page ' + str(currentPageNumber))
		titleTexts, titleLinks = checkLoadPageData(currentPageNumber)
		for index in range(len(titleTexts)):
			data.append(str(titleTexts[index]) + '; ' + str(titleLinks[index]) + '\n')
	fileName = getCurrentDateTimeFormatted() + '.csv'
	print('Writing data to csv file: ' + fileName)
	with open('./savedData/' + fileName, 'w') as f:
		f.write(''.join(data))
	print ("Done")
	
def getLastPageNumber(lastPage):
	"Gets the last page number of the computer game website"
	#https://pcgames-download.com/page/271/ --> 271
	lastPage = lastPage.replace(mainPageUrl + 'page/', "").replace("/", "")
	return int(lastPage)
	
def checkLoadPageData(currentPage):
	"Loads the page data for the given page number"
	if currentPage == 1:
		print (mainPageUrl)
		return loadPageData(mainPageUrl, currentPage)
	else:
		pageUrl = mainPageUrl + 'page/' + str(currentPage)
		print (pageUrl)
		return loadPageData(pageUrl, currentPage)
	
def loadPageData(pageUrl, currentPage):
	"Loads the page data for the given page url"
	response = requests.get(pageUrl)
	pageFile = pagePath + str(currentPage) + '.html'
	with open(pageFile, 'wb') as f:
		f.write(response.content)
	soup = BeautifulSoup(open(pageFile, encoding="utf8"), 'html.parser')
	titleTexts = []
	titleLinks = []
	for posts in soup.find_all(class_='post-title'):
		for post in posts:
			titleTexts.append(post.get('title'))
			titleLinks.append(post.get('href'))
	return (titleTexts, titleLinks)
	
def getCurrentDateTimeFormatted():
	"Returns a string for the json output file with the current date and time"
	return datetime.datetime.now().isoformat().replace(":", "-").replace(".", "-")
	
loadGameData()
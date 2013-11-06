import urllib2
from BeautifulSoup import BeautifulSoup
def valid(link):
	return link.find('/wiki/') != -1 and not link.find(':') != -1 and not link.find('wiktionary') != -1 and not link.find('Main_Page') != -1 and not link.find('(disambiguation)') != -1 and not link.find('List_of') != -1

page = urllib2.urlopen('http://en.m.wikipedia.org/wiki/Special:Random').read()	# Get a random wiki-article
path = [None] * 100
i = 0;
title = ''
while i<100:									# Set a maximum amount of steps to 20
	soup = BeautifulSoup(page)
	title = soup.title.text.split(' -')[0]									
	path[i] = title		# Add the title of the page to the list
	if title == "Philosophy":
		break
	print "Page: " + title
	for anchor in soup.findAll('a', href=True):
    		nextpage = anchor['href']
    		if valid(nextpage):
    			page = urllib2.urlopen("http://en.m.wikipedia.org" + nextpage).read()
    			i = i + 1				
    			break							
print `i` + "steps to Philosophy"
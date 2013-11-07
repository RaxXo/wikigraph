import pickle
import urllib2, sys
from BeautifulSoup import BeautifulSoup
def valid(link):
	return link.find('/wiki/') != -1 and not link.find(':') != -1 and not link.find('wiktionary') != -1 and not link.find('Main_Page') != -1 and not link.find('(disambiguation)') != -1 and not link.find('List_of') != -1

path = [None] * 100
i = 0;
try:
	data = pickle.load(open("data.p","rb"))
except:
	data = {}
title = ''
outer = 0
while outer < 1:
	page = urllib2.urlopen('http://en.wikipedia.org/wiki/Special:Random').read()
	philfound = False
	while i<100:
		soup = BeautifulSoup(page)
		soup.prettify()
		title = soup.title.text.split(' -')[0]		
		print title
		if title in path:
			print "ENDLESS LOOP DETECTED"
			break
		#print span;							
		path[i] = title		# Add the title of the page to the list
		if title == "Philosophy" or title in data.keys():
			philfound = True;
			print "PHILOSOPHY FOUND"
			break
		spans = soup.findAll("p");
		hasnext = False;
		for span in spans:
			for anchor in span.findAll('a', href=True):
		    		nextpage = anchor['href']
		    		if valid(nextpage):
		    			temppage = urllib2.urlopen("http://en.wikipedia.org" + nextpage).read();
		    			soup2 = BeautifulSoup(temppage)
		    			temptitle = soup2.title.text.split(' -')[0]
		    			if temptitle not in path:
		    				page = temppage
		    				hasnext = True
		    				i = i + 1				
		    				break
			if hasnext:
				break

	outer += 1
	if philfound:
		for j in range (0, i):
			if(path[j] in data.keys()):
				if path[j+1] not in data[ path[j] ]:
					data[path[j]].append(path[j+1])
			else:
				data[path[j]] = [ path[j+1] ]
	path = [None] * 100

pickle.dump(data, open("data.p","wb"))
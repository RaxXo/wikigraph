import urllib2
from BeautifulSoup import BeautifulSoup

page = urllib2.urlopen('http://en.wikipedia.org/wiki/Special:Random').read()
soup = BeautifulSoup(page)
soup.prettify()
print soup

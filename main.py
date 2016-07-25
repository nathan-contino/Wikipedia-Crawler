import urllib.request
import re
import hashlib

pagesCollection = {};

class Page(object):
	connections = [];

	def __init__(self, title):
		self.title = title;

	def print_connections(self):
		for c in connections:
			print(c + '\n');
	
	def url(self):
		return 'https://en.wikipedia.org/wiki/' + self.title;
	

def main():
	startPage = Page('Ubuntu_(operating_system)');
	pagesToVisit = [];
	pagesToVisit.append(startPage);
	while pagesToVisit:
		pagesToVisit.extend(fetchPageLinks(pagesToVisit.pop(0)))
	print('donezo');

def fetchPageLinks(page):
	wikipediaURL = page.url();
	local_filename, headers = urllib.request.urlretrieve(wikipediaURL)
	html = open(local_filename)
	goodURLs = filterUnpleasantURLs(findEveryURLOnPage(html.read()))
	
	pageLinks = pageNamesFromURLs(goodURLs);	
	unvisitedGoodPages = removeRepeatURLs(pageLinks);
	
	#now that a Page exists in our Page collection for all of these URLs, link our current Page to each one
	for currPageLink in pageLinks:
		page.connections.append(pagesCollection[currPageLink]);

	pagesToVisit = [];
	for g in unvisitedGoodPages:
		pagesToVisit.append(pagesCollection[g]);
	
	print(',\n'.join(unvisitedGoodPages));
	return pagesToVisit;

def pageNamesFromURLs(urls):
	pageNames = [];
	for u in urls:
		pageNames.append(u.split('/wiki/')[1]);
	return pageNames;

def removeRepeatURLs(pageLinks):
	unvisitedURLs = [];
	for link in pageLinks:
		if not pagesCollection.get(link, False):
			pagesCollection[link] = Page(link);
			unvisitedURLs.append(link);
	return unvisitedURLs;
	

def filterUnpleasantURLs(urls):
	genericWikiPageStart = '/wiki/'
	return [link for link in urls if link.startswith(genericWikiPageStart)];


def findEveryURLOnPage(page):
	#first, we want to filter our page down to just the content
	pageContent = findWikipediaPageBody(page);
	#then use this handy regex to filter things down to just the good stuff (that is, valid wiki pages in english)
	urls = re.findall(r'href=[\'"]?([^\'" >]+)', pageContent)
	return urls;

def findWikipediaPageBody(page):
	contentStartTag = "<div id=\"mw-content-text\" lang=\"en\" dir=\"ltr\" class=\"mw-content-ltr\">";
	return page.partition(contentStartTag)[2];

main(); 

import urllib.request
import re
import hashlib

visitedURLs = {};

def main():
	startPage = '/wiki/Ubuntu_(operating_system)'
	linksToVisit = [];
	linksToVisit.append(startPage);
	while linksToVisit:
		linksToVisit.extend(fetchPageLinks(linksToVisit.pop(0)))
	print('donezo');

def fetchPageLinks(url):
	wikipediaURL = 'https://en.wikipedia.org' + (url);
	local_filename, headers = urllib.request.urlretrieve(wikipediaURL)
	html = open(local_filename)
	goodURLs = filterUnpleasantURLs(findEveryURLOnPage(html.read()))
	unvisitedGoodURLs = removeRepeatURLs(goodURLs);
	print(',\n'.join(unvisitedGoodURLs));
	return unvisitedGoodURLs;

def removeRepeatURLs(urls):
	unvisitedURLs = [];
	for link in urls:
		page_name = link.split('/wiki/')[1]
		if not visitedURLs.get(page_name, False):
			visitedURLs[page_name] = True;
			unvisitedURLs.append(link);
	return unvisitedURLs;
	

def filterUnpleasantURLs(urls):
	genericWikiPageStart = '/wiki/'
	return [link for link in urls if link.startswith(genericWikiPageStart)];


def findEveryURLOnPage(page):
	#first, we want to filter our page down to just the content
	pageContent = findWikipediaPageBody(page);
	urls = re.findall(r'href=[\'"]?([^\'" >]+)', pageContent)
	return urls;

def findWikipediaPageBody(page):
	contentStartTag = "<div id=\"mw-content-text\" lang=\"en\" dir=\"ltr\" class=\"mw-content-ltr\">";
	return page.partition(contentStartTag)[2];

main(); 

import urllib.request
import re

def main():
	local_filename, headers = urllib.request.urlretrieve('https://en.wikipedia.org/wiki/Ubuntu_(operating_system)')
	html = open(local_filename)
	goodURLS = filterUnpleasantURLs(findEveryURLOnPage(html.read()))
	print(','.join(goodURLS));

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

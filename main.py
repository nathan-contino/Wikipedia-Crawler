import urllib.request
local_filename, headers = urllib.request.urlretrieve('http://python.org/')
html = open(local_filename)
print(html.read())


def findEveryURLOnPage(page):
	//first, we want to filter our page down to just the content
	pageContent = findWikipediaPageBody(page);
	return pageContent; //currently just return page content, no url finding


def findWikipediaPageBody(page):
	contentStartTag = "<div id=\"mw-content-text\" lang=\"en\" dir=\"ltr\" class=\"mw-content-ltr\">";
	return page.partition(contentStartTag)[2]; 

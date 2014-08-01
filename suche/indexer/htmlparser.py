'''
htmlparser
takes the raw data from the crawler and
yields various information from the data

copyright(c) 2014 by suche project
'''
from indexer.models import SucheURL
class HTMLParser:
    def __init__(self,text,url):
        self.text = text
        self.url = url

    def parse(self):
        '''
        parse the html content to extract required information
        in required format
        '''
        
        from bs4 import BeautifulSoup, SoupStrainer
        from urllib.parse import urljoin

        # clear the variables
        self.links = []
        
        soup = BeautifulSoup(self.text)

        #first of all, get all the links and their tag in the html page
        for link in soup.find_all('a'):
            filteredurl = SucheURL.filterURL(urljoin(self.url.url,link.get('href')))
            if SucheURL.isvalid(filteredurl): # check if it is a valid URL
                self.links.append((filteredurl,link.text))

    def get_links(self):
        '''
        Returns the list of links on the current document
        '''
        return self.links
        

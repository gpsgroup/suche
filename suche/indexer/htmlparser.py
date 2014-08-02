'''
htmlparser
takes the raw data from the crawler and
yields various information from the data

copyright(c) 2014 by suche project
'''
from indexer.models import SucheURL
import re
import string
from collections import defaultdict

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

        #get the title of the web page and text from the body of the web page

        texts = soup.findAll(text=True)

        visible_texts = filter(HTMLParser.visible, texts)

        # remove symbols from the content and keep only valid english words (and numbers)
        validsymbols =' -' + string.ascii_letters +'0123456789'

        self.content = ''
        for char in ' '.join(visible_texts):
            if char in validsymbols:
                self.content += char
    
        #secondly , make a list of (word,count) tuples
        sentences = self.content.split('.')
        self.words = defaultdict(int)
        for sentence in sentences:
            for word in sentence.split(" "):
                if len(word) >= 2:
                    self.words[word] += 1
        #make a list of word information
        self.wordinfo = ''
        for key in self.words.keys():
            self.wordinfo += key+' = '+str(self.words[key])+'<br/>'
        
  
    def visible(element):
        '''
        represents if the HTML section is visible or not
        '''
        if element.parent.name in ['style', 'script', '[document]', 'head', 'title','iframe']:
            return False
        elif re.match('<!--.*-->', str(element)):
            return False
        return True

    def get_links(self):
        '''
        Returns the list of links on the current document
        '''
        return self.links
    def get_content(self):
        return self.content

    def get_info(self):
        return '<br/><br/>'+self.wordinfo
        

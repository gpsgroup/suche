'''
result.py
contains class for search result
'''
from indexer.models import SucheURL
from linguistic.queryhandler import QueryHandler
import string
import re

class SucheResult:
    def __init__(self):
        self.title = ''

    def getHighlightedTitle(self):
        pass

    def setQuery(self,query):
        self.query = ''
        validsymbols =' ' + string.ascii_letters +'0123456789'
        for char in query:
            if char in validsymbols:
                self.query += char
            else:
                self.query += " "
        self.query = re.sub(' +',' ',self.query)
        self.querylist = self.query.split(' ')
        self.querylist = sorted(self.querylist, key = lambda x:len(x), reverse = True) # sort from largest to smallest word

    def highlightedtitle(self):
        title = self.title
        for key in self.querylist:
            title = title.replace(key,"<strong>"+key+"</strong>")
        return title
    def highlightedurl(self):
        url = self.url
        for key in self.querylist:
            url = url.replace(key,"<strong>"+key+"</strong>")
        return url

    def highlightedbody(self):
        firstoccur = -1
        for key in self.querylist:
            if self.body.find(key) > 0:
                firstoccur = self.body.find(key)
                break
        if firstoccur > -1:
            exstart = firstoccur - 128
            if exstart < 0:
                exstart = 0
            exend = exstart + 250
            if exend > len(self.body)-1:
                exend = len(self.body)-1
            bodyportion = self.body[exstart:exend]
    
        else:
            bodyportion =  self.body[:128]

        for key in self.querylist:
            bodyportion = bodyportion.lower().replace(key,"<strong>"+key+"</strong>")
        return bodyportion


